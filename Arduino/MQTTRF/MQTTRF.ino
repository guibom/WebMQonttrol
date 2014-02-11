// MQTTRF Arduino web controller to RF433 transmitter controller
// Copyright (c) 2014, Guilherme Ramos <longinus@gmail.com>
// https://github.com/guibom/WebMQonttrol
// Released under the MIT license. See LICENSE file for details.

#include <avr/pgmspace.h>
#include <SPI.h>
#include <Ethernet.h>
#include <PubSubClient.h>
#include <VirtualWire.h>

//Buffer for messages
char message_buff[100];

#define STR_ON  "on"
#define STR_OFF "off"
#define STR_0   "0"
#define STR_100 "100"
#define STR_L1_STATUS "home/light/1/status"
#define STR_L1_BRIGHTNESS "home/light/1/status/brightness"

// Update these with values suitable for your network.
byte mac[]    = { 0x00, 0x00, 0x10, 0x66, 0x66, 0x66 };
byte server[] = { 192, 168, 0, 175 };
byte ip[]     = { 192, 168, 0, 20 };

// Callback function header
void callback(char* topic, byte* payload, unsigned int length);

EthernetClient ethClient;
PubSubClient client(server, 1883, callback, ethClient);

// Callback function
void callback(char* topic, byte* payload, unsigned int length) {

    int i = 0;
    byte lightId, lightCmd, lightMax, lightVal;

    //Add payload to message buffer string
    for(i=0; i<length; i++) {
        message_buff[i] = payload[i];
    }
    
    message_buff[i] = '\0';
    String msgString = String(message_buff);

    //Just one light for now, hardcoded values
    lightId = 0xA1;      

    //Light 1, ON
    if (strcmp(topic,"home/light/1/on")==0) {      
        //Check for message
        if (msgString.equals("1")) {
          lightCmd = 0x10;
          lightUpdate(lightId, lightCmd, 100);
          client.publish(STR_L1_STATUS, (uint8_t *)STR_ON, strlen(STR_ON), 1);          
          client.publish(STR_L1_BRIGHTNESS, (uint8_t *)STR_100, strlen(STR_100), 1);
        }
    }

    //Light 1, Off
    if (strcmp(topic,"home/light/1/off")==0) {
        //Check for message
        if (msgString.equals("1")) {
          lightCmd = 0x10;
          lightUpdate(lightId, lightCmd, 0);
          client.publish(STR_L1_STATUS, (uint8_t *)STR_OFF, strlen(STR_OFF), 1);   
          client.publish(STR_L1_BRIGHTNESS, (uint8_t *)STR_0, strlen(STR_0), 1);
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
          client.publish(STR_L1_STATUS, (uint8_t *)STR_ON, strlen(STR_ON), 1);    
        else
          client.publish(STR_L1_STATUS, (uint8_t *)STR_OFF, strlen(STR_OFF), 1);

        //Convert int to char*
        // char b_payload[4];
        // sprintf(b_payload, "%d", bvalue);
        
        byte byteBuf[4];  
        msgString.getBytes(byteBuf, sizeof(byteBuf));
    
        client.publish(STR_L1_BRIGHTNESS, byteBuf, 3, 1);
    }

    //Light 1, Fade_on
    if (strcmp(topic,"home/light/1/fade_on")==0) {
        lightCmd = 0x20;
        lightUpdate(lightId, lightCmd, msgString.toInt(), msgString.toInt());

        client.publish(STR_L1_STATUS, (uint8_t *)STR_ON, strlen(STR_ON), 1);
        client.publish(STR_L1_BRIGHTNESS, (uint8_t *)STR_100, strlen(STR_100), 1);
    }

    //Light 1, Fade_off
    if (strcmp(topic,"home/light/1/fade_off")==0) {
          lightCmd = 0x30;
          lightUpdate(lightId, lightCmd, msgString.toInt(), msgString.toInt());

        client.publish(STR_L1_STATUS, (uint8_t *)STR_OFF, strlen(STR_OFF), 1);
        client.publish(STR_L1_BRIGHTNESS, (uint8_t *)STR_0, strlen(STR_0), 1);
    }

    // char charBuf[50];  
    // msgString.toCharArray(charBuf, 50);
}

//Maxium val on lightMax
void lightUpdate(byte lightId, byte lightCmd, int val)
{
  lightUpdate(lightId, lightCmd, val, 0xFF);
}

//Configurable val on lightMax
void lightUpdate(byte lightId, byte lightCmd, int val, byte lightMax)
{
    char *msg = "0000";
    msg[0] = lightId;  //Light ID
    msg[1] = lightCmd;  //Command: 0x10 sets light.=
    msg[2] = lightMax;  //Max values the light will take
    msg[3] = map(val,0,100,0,255); //Actualy value being sent

    //Send RF message
    vw_send((uint8_t *)msg, strlen(msg));
    vw_wait_tx(); // Wait until the whole message is gone
}

void setup()
{  
    Ethernet.begin(mac, ip);
    if (client.connect("MQTTRF", "home/controller/MQTTRF", 0, 1, STR_OFF)) {
        //Publish controller abilities and conencted hardware
        client.publish("home/controller/MQTTRF", (uint8_t *)"on", 2, 1);
        client.publish("home/controller/MQTTRF/light/1", (uint8_t *)"1", 1, 1);
        
        //Subscriptions
        client.subscribe("home/light/1/#");
        client.subscribe("home/light/all/#");
    }

  //RF433 Setup
  vw_set_tx_pin(2);
  vw_set_rx_pin(5);
  vw_set_ptt_pin(1);
  vw_setup(1000);  // Bits per sec
}

void loop()
{
    client.loop();
}