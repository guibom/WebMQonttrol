// MQTTRF Arduino web gateway to RF433 transmitter controller
// Copyright (c) 2014, Guilherme Ramos <longinus@gmail.com>
// https://github.com/guibom/WebMQonttrol
// Released under the MIT license. See LICENSE file for details.

//If true, prints debug messages to serial
#define DEBUG       false
#define DEBUG_MEM   false
#define PUBLISH_MEM true

//Libraries
#include <JsonParser.h>
#include <SPI.h>
#include <Ethernet.h>
#include <EthernetUdp.h>
#include <PubSubClient.h>
#include <VirtualWire.h>
#include <x10.h>
#include <x10constants.h>
#include <avr/pgmspace.h>
#include <Streaming.h>
#include <MemoryFree.h>
#include <RCSwitch.h>
#include <Metro.h>

//IO Pin Constants
#define PIN_STATUS_LED      A5
#define PIN_X10_ZERO_CROSS  9
#define PIN_X10_DATA        8
#define PIN_RFSWITCH        7
#define PIN_VWIRE_TX        2
#define PIN_VWIRE_RX        5
#define PIN_VWIRE_PTT       1

//Publish free memory over MQTT every 5min
#if PUBLISH_MEM
  Metro memMetro = Metro(300000);
#endif

EthernetUDP Udp;
unsigned int UDPPort = 666; // local port to listen on

// buffers for receiving and sending data
char packetBuffer[UDP_TX_PACKET_MAX_SIZE]; //buffer to hold incoming packet,
char ReplyBuffer[] = "1";       // a string to send back

//315Mhz RF Switch
RCSwitch mySwitch = RCSwitch();

//Set up a new x10 instance
x10 myHouse =  x10(PIN_X10_ZERO_CROSS, PIN_X10_DATA);

//X10 Json parser
JsonParser<8> parser;

//Buffer for messages/progmem topics
char buffer[64];

#define TOPIC_ARRAY_SIZE 8
char* topicElements[TOPIC_ARRAY_SIZE];
const char topicDelimiter[] = "/";

//Standard messages used
#define STR_ON      "on"
#define STR_OFF     "off"
#define STR_ONLINE  "online"
#define STR_OFFLINE "offline"
#define STR_1       "1"
#define STR_0       "0"
#define STR_100     "100"

//PROGMEM Topics
const char STR_GATEWAY[] PROGMEM = "home/gateway/mqttrf";
const char STR_GATEWAY_L1[] PROGMEM = "home/gateway/mqttrf/light/1";
const char STR_GATEWAY_X10[] PROGMEM = "home/gateway/mqttrf/x10";
const char STR_GATEWAY_RFSWITCH[] PROGMEM = "home/gateway/mqttrf/rfswitch";

const char STR_GATEWAY_RAM[] PROGMEM = "home/gateway/mqttrf/memory/free";

const char STR_L1_STATUS[] PROGMEM = "home/light/1/status";
const char STR_L1_BRIGHTNESS[] PROGMEM = "home/light/1/status/brightness";

const char STR_X10_STATUS[] PROGMEM = "home/x10/status";
const char STR_RFSWITCH_STATUS[] PROGMEM = "home/rfswitch/status/raw";

//PROGMEM Subscription topics. Automatically subscribe to all of them at the start
#define STR_TOPICS_SIZE 3  //Needs to reflect the actual number of topics needed
prog_char P_STR_SUB_L_1[] PROGMEM = {"home/light/+/action/#"};
prog_char P_STR_SUB_X10[] PROGMEM = {"home/x10/action/#"};
prog_char P_STR_SUB_RFSWITCH[] PROGMEM = {"home/rfswitch/action"};

//Holds all the subscriptions.
PROGMEM const char *string_topics[] = {P_STR_SUB_L_1, P_STR_SUB_X10, P_STR_SUB_RFSWITCH };


//House Codes Topics
prog_char topic_house[] PROGMEM = {"ABCDEFGHIJKLMNOP"};
//House Code Constants
PROGMEM prog_uint8_t constant_house[] = {A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P};

//Unit Code Constant
PROGMEM prog_uint8_t constant_unit[] = {UNIT_1, UNIT_2, UNIT_3, UNIT_4, UNIT_5, UNIT_6, UNIT_7, UNIT_8, UNIT_9, UNIT_10, UNIT_11, UNIT_12, UNIT_13, UNIT_14, UNIT_15, UNIT_16};

//Command Codes
prog_char CMD_1[] PROGMEM = {"ALL_LIGHTS_ON"};
prog_char CMD_2[] PROGMEM = {"ALL_UNITS_OFF"};
prog_char CMD_3[] PROGMEM = {"ON"};
prog_char CMD_4[] PROGMEM = {"OFF"};
prog_char CMD_5[] PROGMEM = {"DIM"};
prog_char CMD_6[] PROGMEM = {"BRIGHT"};
prog_char CMD_7[] PROGMEM = {"ALL_LIGHTS_OFF"};
prog_char CMD_8[] PROGMEM = {"EXTENDED_CODE"};
prog_char CMD_9[] PROGMEM = {"HAIL_REQUEST"};
prog_char CMD_10[] PROGMEM = {"HAIL_ACKNOWLEDGE"};
prog_char CMD_11[] PROGMEM = {"PRE_SET_DIM"};
prog_char CMD_12[] PROGMEM = {"EXTENDED_DATA"};
prog_char CMD_13[] PROGMEM = {"STATUS_ON"};
prog_char CMD_14[] PROGMEM = {"STATUS_OFF"};
prog_char CMD_15[] PROGMEM = {"STATUS_REQUEST"};

//Array of Command Codes
PROGMEM const char *topic_command[] = {CMD_1,CMD_2,CMD_3,CMD_4,CMD_5,CMD_6,CMD_7,CMD_8,CMD_9,CMD_10,CMD_11,CMD_12,CMD_13,CMD_14,CMD_15};
//Command Code constants
PROGMEM prog_uint8_t constant_command[] = {ALL_LIGHTS_ON,ALL_UNITS_OFF,ON,OFF,DIM,BRIGHT,ALL_LIGHTS_OFF,EXTENDED_CODE,HAIL_REQUEST,HAIL_ACKNOWLEDGE,PRE_SET_DIM,EXTENDED_DATA,STATUS_ON,STATUS_OFF,STATUS_REQUEST};

//The section in the MQTT topic array that the specific X10 codes are
#define X10_HOUSE_N   3
#define X10_UNIT_N    X10_HOUSE_N + 1
#define X10_CMD_N     X10_UNIT_N + 1


//Hardcoded network address
byte mac[]    = { 0x00, 0x00, 0x10, 0x66, 0x66, 0x66 };
byte server[] = { 192, 168, 0, 175 };
byte ip[]     = { 192, 168, 0, 20 };

// Callback function header
void callback(char* topic, byte* payload, unsigned int length);

//Ethernet and MQTT client
EthernetClient ethClient;
PubSubClient client(server, 1883, callback, ethClient);


//MQTT Callback function
void callback(char* topic, byte* payload, unsigned int length) {

  //Convert payload to char array
  char *cpayload = (char *) payload;
  cpayload[length] = '\0';

  #if DEBUG 
    Serial << "Message received: [" << topic << "] [" << cpayload << "]" << endl;
  #endif
  #if DEBUG_MEM
    Serial << "MEM: " << freeMemory() << endl;
  #endif


  //Light 1 ACTIONS **************************************************
  if (strncmp(topic,"home/light/1/action/", 20)==0) {

    byte lightId, lightCmd, lightMax, lightVal;
    //Just one light for now, hardcoded values
    lightId = 0xA1;

    //Split topic elements
    strcpy(buffer, topic);
    fillTopicElements();

    //ON    
    if (strcmp(topicElements[4], "on")==0) {
      //Check for message
      if (strcmp(cpayload, "1")==0) {
        lightCmd = 0x10;
        lightUpdate(lightId, lightCmd, 100);
        
        Publish(STR_L1_STATUS, STR_ON, true);
        Publish(STR_L1_BRIGHTNESS, STR_100, true);    
      }
    }

    //OFF
    if (strcmp(topicElements[4], "off")==0) {
      //Check for message
      if (strcmp(cpayload, "1")==0) {
        lightCmd = 0x10;
        lightUpdate(lightId, lightCmd, 0);

        Publish(STR_L1_STATUS, STR_OFF, true);
        Publish(STR_L1_BRIGHTNESS, STR_0, true);
      }
    }

    //SET
    if (strcmp(topicElements[4], "set")==0) {
      lightCmd = 0x10;
      int bvalue = atoi(cpayload);

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

      //Convert int to char*
      char b_payload[4];
      sprintf(b_payload, "%d", bvalue);
        
      Publish(STR_L1_BRIGHTNESS, b_payload, true); 
    }

    //FADE_ON
    if (strcmp(topicElements[4], "fade_on")==0) {
      lightCmd = 0x20;
      lightUpdate(lightId, lightCmd, atoi(cpayload), atoi(cpayload));

      Publish(STR_L1_STATUS, STR_ON, true);
      Publish(STR_L1_BRIGHTNESS, STR_100, true);
    }

    //FADE_OFF
    if (strcmp(topicElements[4], "fade_off")==0) {
      lightCmd = 0x30;
      lightUpdate(lightId, lightCmd, atoi(cpayload), atoi(cpayload));
      
      Publish(STR_L1_STATUS, STR_OFF, true);
      Publish(STR_L1_BRIGHTNESS, STR_0, true);
    }
  }


  //X10 ACTIONS ******************************************************
  if (strncmp(topic,"home/x10/action/", 16)==0) {

    //Split topic elements
    strcpy(buffer, topic);
    fillTopicElements();

    //Loop over all HOUSES
    for (uint8_t h = 0; h < 17; h++) {

      //Copy house codes from PROGMEM
      char b_topic_house[2] = {pgm_read_byte(topic_house + h)};
      byte b_constant_house = pgm_read_byte_near(constant_house + h);

      //Check house code match
      if (strcmp(topicElements[X10_HOUSE_N], b_topic_house)==0) {

        //Loop over all UNITS
        for (int u = 0; u < 16; u++) {

          //Create a UNIT_XX string based on the loop number
          char b_topic_unit[8] = "UNIT_";
          char b_topic_unit_numb[3];
          itoa(u + 1, b_topic_unit_numb, 10);
          strncat (b_topic_unit, b_topic_unit_numb, 2);

          //Copy unit codes from PROGMEM
          byte b_constant_unit = pgm_read_byte_near(constant_unit + u);
          
          //Check unit code match
          if (strcmp(topicElements[X10_UNIT_N], b_topic_unit)==0) {            

            //Loop over all HOUSES
            for (uint8_t c = 0; c < 16; c++) {

              //Copy command codes from PROGMEM              
              strcpy_P(buffer, (char*)pgm_read_word(&(topic_command[c])));    
              byte b_constant_command = pgm_read_byte_near(constant_command + c);              

              //Check command for match
              if (strcmp(topicElements[X10_CMD_N], buffer)==0) {          

                //Payload is the number of tries
                int bvalue = atoi(cpayload);     

                #if DEBUG                
                  Serial << "X10 Action: " << b_topic_house << ":" << b_constant_house << "/" << b_topic_unit << ":" << b_constant_unit << "/" << buffer << ":" << b_constant_command << " -- Try: " << bvalue << endl;
                #endif               

                //Execute X10 Command
                myHouse.write(b_constant_house, b_constant_unit, bvalue);
                myHouse.write(b_constant_house, b_constant_command, bvalue);
                
                //Acknowledge X10 status by publishing the received topic in a status message
                char X10ACK[26]; 
                sprintf(X10ACK, "%s", topic + 16);
                Publish(STR_X10_STATUS, X10ACK, false);

                //Stop checking
                return;
              }
            }
          }
        }       
      }
    }
  }


  //315 RF Switch ACTIONS ********************************************
  if (strncmp(topic,"home/rfswitch/action", 20)==0) {

    //Copy payload first    
    char JsonACK[strlen(cpayload)+1];    
    strcpy (JsonACK,cpayload);

    //Parse JSON payload -- Format {"D":123456,"B":24}
    JsonHashTable hashTable = parser.parseHashTable(cpayload);

    //Failed (bigger then buffer?)
    if (!hashTable.success()) {
      #if DEBUG                
        Serial << "JSON Parser failed!" << endl;
      #endif
      return;
    }

    //Send RFSwitch command
    mySwitch.send(hashTable.getLong("D"), hashTable.getLong("B"));
    //mySwitch.send(1393741, 24);
    //mySwitch.send(1393777, 24);

    //Parsed JSON OK!
    #if DEBUG                
      Serial << "RFSwitch Action: " << hashTable.getLong("D") << " Decimal, " << hashTable.getLong("B") << "bits" << endl;
    #endif

    //Acknowledge RFSwitch command by publishing the same message 
    Publish(STR_RFSWITCH_STATUS, JsonACK, false);
  }

}

//Fill array with split topic elements
void fillTopicElements() {

  char* valPosition, *p;  

  valPosition = strtok_r(buffer, topicDelimiter, &p);  

  for (uint8_t i=0; i < TOPIC_ARRAY_SIZE; i++) {

    if (valPosition != NULL) {
      topicElements[i] = valPosition;
      valPosition = strtok_r(NULL, topicDelimiter, &p);
    } else {
      topicElements[i] = '\0';
    }
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
  pinMode(PIN_STATUS_LED, OUTPUT);
  digitalWrite(PIN_STATUS_LED, HIGH);
  
  //Ethernet connection
  Ethernet.begin(mac, ip);

  #if DEBUG    
    Serial.println("Connected to Ethernet");
  #endif

  //Start UPD daemon
  Udp.begin(UDPPort);

  #if DEBUG    
    Serial.println("Opened UDP Port");
  #endif

  //Try to connect to MQTT server
  if (client.connect("MQTTRF", getString(STR_GATEWAY), 0, 1, STR_OFFLINE)) {

    #if DEBUG
        Serial.println("Connected to MQTT broker");
    #endif

    //Publish gateway abilities and conencted hardware
    Publish(STR_GATEWAY, STR_ONLINE, true);
    Publish(STR_GATEWAY_L1, STR_ONLINE, true);
    Publish(STR_GATEWAY_X10, STR_ONLINE, true);
    Publish(STR_GATEWAY_RFSWITCH, STR_ONLINE, true);
          
    //Subscribe to topics defined in PROGMEM array
    subscribeTopics();

    //Set status light to ON
    digitalWrite(PIN_STATUS_LED, LOW);

    //RF433 Setup
    vw_set_tx_pin(PIN_VWIRE_TX);
    vw_set_rx_pin(PIN_VWIRE_RX);
    vw_set_ptt_pin(PIN_VWIRE_PTT);
    vw_setup(1000);  // Bits per sec

    //RF315 Switch Setup
    mySwitch.enableTransmit(PIN_RFSWITCH);


    #if DEBUG
        Serial.println("Virtual Wire and RF Switch configured.");
    #endif
    #if DEBUG_MEM
        Serial << "MEM: " << freeMemory() << endl;
    #endif


  //Failed to connect to server
  } else {
    
    #if DEBUG    
      Serial.println("Failed to connect to MQTT broker!");
    #endif

    //Blink status light
    while(1) {
      digitalWrite(PIN_STATUS_LED, LOW);
      delay(250);
      digitalWrite(PIN_STATUS_LED, HIGH);
      delay(250);
    }
  }
}

//Default loop, just process MQTT messages & Metro actions
void loop() {

  //MQTT loop  
  client.loop();

  //UDP admin loop
  checkUDP();

  #if PUBLISH_MEM
    // check if the metro has passed its interval
    if (memMetro.check() == 1) { 
      Publish_FreeMem();
    }
  #endif
}

//Subscribe to list of topics in PROGMEM
void subscribeTopics() {

  //Loop over all the topics defined in PROGMEM
  for (int i = 0; i < STR_TOPICS_SIZE; i++) {
    strcpy_P(buffer, (char*)pgm_read_word(&(string_topics[i])));    
    client.subscribe(buffer);  //MQTT Subscribe

    #if DEBUG            
        Serial << "Subscribed to topic: " << buffer << endl;
    #endif
  }
}

//Return char string from PROGMEM
char* getString(const char* str) {
  strcpy_P(buffer, (char*)str);
  return buffer;
}

//Uses topic in PROGMEM, autosize payload
boolean Publish(const char* topic, char* payload, boolean retained) {
  
  //Publish message
  bool res = client.publish(getString(topic), (uint8_t*)payload, strlen(payload), retained); 

  #if DEBUG
      Serial << "Message sent: [" << getString(topic) << "] [" << payload << "]" << endl;
  #endif
  #if DEBUG_MEM
      Serial << "MEM: " << freeMemory() << endl;
  #endif

  return res;
}

//Publish the amount of Free Memory to MQTT
boolean Publish_FreeMem() {
  char mem[4];
  sprintf(mem, "%d", freeMemory());  

  return client.publish(getString(STR_GATEWAY_RAM), (uint8_t*)mem, strlen(mem), true);
}

//Check Magic packet in UDP, soft reset if kill command found
void checkUDP() {

  // if there's data available, read a packet
  int packetSize = Udp.parsePacket();
  
  if(packetSize) {    
    char contents = Udp.read();    
    // send a reply, to the IP address and port that sent us the packet we received
    Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
    
    if (contents == 'K') {

      Udp.write('1');      
      Udp.endPacket();

      #if DEBUG            
        Serial << "RESETTING..." << endl;
      #endif
      
      //Software Reset
      software_Reset();

    } else {

      Udp.write('0');
      Udp.endPacket();
    }        
  }
}

// Restarts program from beginning but does not reset the peripherals and registers
void software_Reset() {
  asm volatile ("  jmp 0");
}

//Return size of PROGMEM variable
// byte size(prog_uchar *var) {
//   return sizeof(var)-1;
// }