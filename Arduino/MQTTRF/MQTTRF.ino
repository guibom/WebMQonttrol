// MQTTRF Arduino web gateway to RF433 transmitter controller
// Copyright (c) 2014, Guilherme Ramos <longinus@gmail.com>
// https://github.com/guibom/WebMQonttrol
// Released under the MIT license. See LICENSE file for details.

//If true, prints debug messages to serial
#define DEBUG     true
#define DEBUG_MEM false

#include <JsonParser.h>
#include <SPI.h>
#include <Ethernet.h>
#include <PubSubClient.h>
#include <VirtualWire.h>
#include <x10.h>
#include <x10constants.h>
#include <avr/pgmspace.h>
#include <Streaming.h>
#if DEBUG_MEM
  #include <MemoryFree.h>
#endif

//IO Pin Constants
#define STATUS_LED      A5
#define X10_ZERO_CROSS  9
#define X10_DATA        8

//Set up a new x10 instance
x10 myHouse =  x10(X10_ZERO_CROSS, X10_DATA);

//Buffer for messages
char buffer[64];
char buffer_topic[64];

#define STR_ON  "on"
#define STR_OFF "off"
#define STR_0   "0"
#define STR_100 "100"

//PROGMEM strings for TOPICS
#define STR_GATEWAY       0
#define STR_GATEWAY_L1    1
#define STR_L1_STATUS     2
#define STR_L1_BRIGHTNESS 3

//PROGMEM Topics
prog_char P_STR_GATEWAY[] PROGMEM = {"home/gateway/MQTTRF"};
prog_char P_STR_GATEWAY_L1[] PROGMEM = {"home/gateway/MQTTRF/light/1"};

prog_char P_STR_L1_STATUS[] PROGMEM = {"home/light/1/status"};
prog_char P_STR_L1_BRIGHTNESS[] PROGMEM = {"home/light/1/status/brightness"};

//Array that holds all the PROGMEM topic strings
PROGMEM const char *string_table[] =
{   
  P_STR_GATEWAY,        //0
  P_STR_GATEWAY_L1,     //1
  P_STR_L1_STATUS,      //2
  P_STR_L1_BRIGHTNESS,  //3
};

//PROGMEM Subscription topics. Automatically subscribe to all of them at the start
#define STR_TOPICS_SIZE 2  //Needs to reflect the actual number of topics needed
prog_char P_STR_SUB_L_ALL[] PROGMEM = {"home/light/all/#"};
prog_char P_STR_SUB_L_1[] PROGMEM = {"home/light/1/#"};

//Holds all the subscriptions.
PROGMEM const char *string_topics[] =
{   
  P_STR_SUB_L_ALL,
  P_STR_SUB_L_1
};

//PROGMEM strings for MESSAGES
// prog_uchar STR_TMP_ON[] PROGMEM = {"on"};
// prog_uchar STR_TMP_OFF[] PROGMEM = {"off"};
// prog_uchar STR_TMP_0[] PROGMEM = {"0"};
// prog_uchar STR_TMP_1[] PROGMEM = {"1"};
// prog_uchar STR_TMP_100[] PROGMEM = {"100"};

// Update these with values suitable for your network.
byte mac[]    = { 0x00, 0x00, 0x10, 0x66, 0x66, 0x66 };
byte server[] = { 192, 168, 0, 175 };
byte ip[]     = { 192, 168, 0, 20 };

// Callback function header
void callback(char* topic, byte* payload, unsigned int length);

EthernetClient ethClient;
PubSubClient client(server, 1883, callback, ethClient);

//Json
JsonParser<12> parser;

// Callback function
void callback(char* topic, byte* payload, unsigned int length) {

    int i = 0;
    byte lightId, lightCmd, lightMax, lightVal;

    //Add payload to message buffer string
    for(i=0; i<length; i++) {
        buffer[i] = payload[i];
    }
           
    buffer[i] = '\0';
    String msgString = String(buffer);

    #if DEBUG            
      //Serial.print("Message received: "); Serial.print(topic); Serial.print(" "); Serial.println(msgString);
      Serial << "Message received: " << topic << " " << msgString << endl;
    #endif
    #if DEBUG_MEM
      Serial << "MEM: " << freeMemory() << endl;
      // Serial.print("MEM: "); Serial.println(freeMemory());
    #endif

    //Just one light for now, hardcoded values
    lightId = 0xA1;      

    //Light 1, ON
    if (strcmp(topic,"home/light/1/on")==0) {      
      //Check for message
      if (msgString.equals("1")) {
        lightCmd = 0x10;
        lightUpdate(lightId, lightCmd, 100);
        
        Publish(STR_L1_STATUS, STR_ON, true);
        Publish(STR_L1_BRIGHTNESS, STR_100, true);

      }
    }

    //Light 1, Off
    if (strcmp(topic,"home/light/1/off")==0) {
      //Check for message
      if (msgString.equals("1")) {
        lightCmd = 0x10;
        lightUpdate(lightId, lightCmd, 0);

        Publish(STR_L1_STATUS, STR_OFF, true);
        Publish(STR_L1_BRIGHTNESS, STR_0, true);
      }
    }

    //Light 1, Set
    if (strcmp(topic,"home/light/1/set")==0) {
      lightCmd = 0x10;
      int bvalue = msgString.toInt();

      //Clamp payload to safe numbers
      if (bvalue > 100)
        bvalue = 100;
      else if (bvalue < 0)
        bvalue = 0;

      lightUpdate(lightId, lightCmd, bvalue);

      if (bvalue > 0)          
        Publish(STR_L1_STATUS, STR_ON, true);
      else                  
        Publish(STR_L1_STATUS, STR_OFF, true);
      
      //byte byteBuf[4];  
      //msgString.getBytes(byteBuf, sizeof(byteBuf));

      //Convert int to char*
      char b_payload[4];
      sprintf(b_payload, "%d", bvalue);
        
      Publish(STR_L1_BRIGHTNESS, b_payload, true);
    }

    //Light 1, Fade_on
    if (strcmp(topic,"home/light/1/fade_on")==0) {
      lightCmd = 0x20;
      lightUpdate(lightId, lightCmd, msgString.toInt(), msgString.toInt());

      Publish(STR_L1_STATUS, STR_ON, true);
      Publish(STR_L1_BRIGHTNESS, STR_100, true);
    }

    //Light 1, Fade_off
    if (strcmp(topic,"home/light/1/fade_off")==0) {
      lightCmd = 0x30;
      lightUpdate(lightId, lightCmd, msgString.toInt(), msgString.toInt());
      
      Publish(STR_L1_STATUS, STR_OFF, true);
      Publish(STR_L1_BRIGHTNESS, STR_0, true);
    }

    //X10
    if (strcmp(topic,"home/x10/action")==0) {           
    //      String house = getValue(msgString, ',', 0);
    //      String unit = getValue(msgString, ',', 1);
    //      String action = getValue(msgString, ',', 2);
    //      String tries = getValue(msgString, ',', 3);      
    //      
    //       char charBuf[30];  
    //       msgString.toCharArray(charBuf, 30);
    //      
    //      JsonHashTable hashTable = parser.parseHashTable(charBuf);
    //  
    //      if (!hashTable.success())
    //      {
    //          Serial.println("JsonParser.parseHashTable() failed");
    //          return;
    //      }
    //
    //      char charBuf[10];     
    //      msgString.toCharArray(charBuf, 10);          
    //    
    //      //Check for message
    //      myHouse.write(house.toInt(), unit.toInt(), tries.toInt());
    //      myHouse.write(house.toInt(), action.toInt(), tries.toInt());
    //      
    //      client.publish("home/x10/status", charBuf);

      //{"H":0,"U":2,"A":99,"R":3}
    }
}

//Maxium val on lightMax
void lightUpdate(byte lightId, byte lightCmd, int val) {
  lightUpdate(lightId, lightCmd, val, 0xFF);
}

//Configurable val on lightMax
void lightUpdate(byte lightId, byte lightCmd, int val, byte lightMax) {

    char *msg = "0000";
    msg[0] = lightId;  //Light ID
    msg[1] = lightCmd;  //Command: 0x10 sets light.=
    msg[2] = lightMax;  //Max values the light will take
    msg[3] = map(val,0,100,0,255); //Actualy value being sent

    //Send RF message
    vw_send((uint8_t *)msg, strlen(msg));
    vw_wait_tx(); // Wait until the whole message is gone
}


//----- SETUP ---------
void setup() {

  //Serial Debug if enabled
  #if DEBUG || DEBUG_MEM    
    Serial.begin(57600);
    Serial.println("Started");
  #endif
         
  //Set status light OFF by default. Enabled low.
  pinMode(STATUS_LED, OUTPUT);
  digitalWrite(STATUS_LED, HIGH);
  
  //Ethernet connection
  Ethernet.begin(mac, ip);

  #if DEBUG    
    Serial.println("Connected to Ethernet");
  #endif

  //Try to connect to MQTT server        
  if (client.connect("MQTTRF", "home/gateway/MQTTRF", 0, 1, STR_OFF)) {
    #if DEBUG    
      Serial.println("Connected to MQTT broker");
    #endif

    //Publish gateway abilities and conencted hardware    
    Publish(STR_GATEWAY, STR_ON, true);
    Publish(STR_GATEWAY_L1, "1", true);    
          
    //Subscribe to topics defined in PROGMEM array
    subscribeTopics();

    //Set status light to ON
    digitalWrite(STATUS_LED, LOW);

  } else {
    //Failed to connect to server
    #if DEBUG    
      Serial.println("Failed to connect to MQTT broker!");
    #endif

    //Blink status light
    while(1) {
      digitalWrite(STATUS_LED, LOW);
      delay(250);
      digitalWrite(STATUS_LED, HIGH);
      delay(250);
    }
  }

  //RF433 Setup
  vw_set_tx_pin(2);
  vw_set_rx_pin(5);
  vw_set_ptt_pin(1);
  vw_setup(1000);  // Bits per sec
  
  #if DEBUG_MEM
      Serial.print("MEM: "); Serial.println(freeMemory());
  #endif
}

//Default loop, just process MQTT messages
void loop() {
    client.loop();
}

//Subscribe to list of topics in PROGMEM
void subscribeTopics() {

  for (int i = 0; i < STR_TOPICS_SIZE; i++) {
    strcpy_P(buffer_topic, (char*)pgm_read_word(&(string_topics[i])));    
    client.subscribe(buffer_topic);  //MQTT Subscribe

    #if DEBUG    
        Serial.print("Subscribed to topic: "); Serial.println(buffer_topic);
    #endif
  }  
}

char *returnTopic(uint8_t i) {    
    strcpy_P(buffer_topic, (char*)pgm_read_word(&(string_table[i])));
    return buffer_topic;
}

//Uses topic in PROGMEM
boolean Publish(uint8_t topic, char* payload, boolean retained) {
  
  //Publish message
  client.publish(returnTopic(topic), (uint8_t*)payload, strlen(payload), retained); 

  #if DEBUG
      //Add payload to message buffer string
      int i;
      for(i=0; i<strlen(payload); i++)
          buffer[i] = payload[i];
             
      buffer[i] = '\0';
      String msgString = String(buffer);

      Serial.print("Message sent: "); Serial.print(returnTopic(topic)); Serial.print(" "); Serial.println(msgString);
  #endif
  #if DEBUG_MEM
      Serial.print("MEM: "); Serial.println(freeMemory());
  #endif

}

//Return size of PROGMEM variable
byte size(prog_uchar *var) {
  return sizeof(var)-1;
}