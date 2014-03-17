// LED Light Bar
// Copyright (c) 2014, Guilherme Ramos <longinus@gmail.com>
// https://github.com/guibom/WebMQonttrol
// Released under the MIT license. See LICENSE file for details.
// Uses Attiny85 + 433 RF receiver

#include <avr/pgmspace.h>
#include <VirtualWire.h>

#include <avr/sleep.h>
#include <avr/interrupt.h>

// CIE Lightness lookup table function
#define CIELPWM(a) (pgm_read_byte_near(CIEL8 + a))
#define FULLCIELPWM(a) (pgm_read_byte_near(CIEL256 + a))

//LED MOSFET Pin
#define LED_PIN 4

//ID of this light
#define LIGHT_ID 0xA1

//Types of command the light can receive
#define LIGHT_CMD_SET       0x10
#define LIGHT_CMD_FADEUP    0x20
#define LIGHT_CMD_FADEDOWN  0x30


//Starting light value
int light_val = 0;

//CIE Lookup table, 64 values
prog_uint8_t CIEL8[] PROGMEM = {
  0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 
  5, 6, 7, 8, 9, 10, 12, 13, 14, 16, 
  18, 20, 22, 24, 26, 28, 31, 33, 36, 39, 
  42, 45, 49, 52, 56, 60, 64, 68, 73, 77, 
  82, 87, 92, 98, 103, 109, 115, 122, 128, 135, 
  142, 149, 156, 164, 172, 180, 189, 197, 206, 215, 
  225, 235, 245, 255
};

//CIE Lookup table for fades, 256 values
prog_uint8_t CIEL256[] PROGMEM = {
  0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 
  1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 
  2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 
  3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 
  5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 
  7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 
  10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 
  13, 14, 14, 15, 15, 15, 16, 16, 17, 17, 
  17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 
  22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 
  28, 28, 29, 29, 30, 31, 31, 32, 32, 33, 
  34, 34, 35, 36, 37, 37, 38, 39, 39, 40, 
  41, 42, 43, 43, 44, 45, 46, 47, 47, 48, 
  49, 50, 51, 52, 53, 54, 54, 55, 56, 57, 
  58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 
  68, 70, 71, 72, 73, 74, 75, 76, 77, 79, 
  80, 81, 82, 83, 85, 86, 87, 88, 90, 91, 
  92, 94, 95, 96, 98, 99, 100, 102, 103, 105, 
  106, 108, 109, 110, 112, 113, 115, 116, 118, 120, 
  121, 123, 124, 126, 128, 129, 131, 132, 134, 136, 
  138, 139, 141, 143, 145, 146, 148, 150, 152, 154, 
  155, 157, 159, 161, 163, 165, 167, 169, 171, 173, 
  175, 177, 179, 181, 183, 185, 187, 189, 191, 193, 
  196, 198, 200, 202, 204, 207, 209, 211, 214, 216, 
  218, 220, 223, 225, 228, 230, 232, 235, 237, 240, 
  242, 245, 247, 250, 252, 255 
};


void setup()
{
  //Callibration stuff for 8mhz Attiny
  OSCCAL = 0x8F;

  //Power-saving settings
  ACSR |= _BV(ACD);       //disable the analog comparator
  ADCSRA &= ~_BV(ADEN);   //disable ADC

  //Receive pin
  vw_set_rx_pin(2);

  // Initialise the IO and ISR
  vw_setup(1000);	 // Bits per sec

  // Start the receiver PLL running
  vw_rx_start();       

  //Set LED pin as output
  pinMode(LED_PIN, OUTPUT);

  //Smoothly fade the light up
  fadeUp(50);

  // Serial.begin(9600); // Debugging only
  // Serial.println("Receiver");

}

void loop()
{
  //Manchester buffers
  uint8_t buf[VW_MAX_MESSAGE_LEN];
  uint8_t buflen = VW_MAX_MESSAGE_LEN;

  // Non-blocking check for message
  if (vw_get_message(buf, &buflen)) 
  {	
    //Check if the message is for this light
    if (buf[0] == LIGHT_ID)
    {
      //Command received
      switch (byte(buf[1])) {
        //Set light to value
        case LIGHT_CMD_SET:
          if (byte(buf[2]) == 0) 
            updateLight(byte(buf[3]));
          else
            updateLight(byte(buf[3]),byte(buf[2]));
          break;
        //Fade up, speed, to value
        case LIGHT_CMD_FADEUP:
          fadeUp(byte(buf[2]));
          break;
        //Fade down, speed, to value
        case LIGHT_CMD_FADEDOWN:
          fadeDown(byte(buf[2]));
          break;
      }
    }
  }
}

//Set the light to a raw value
void updateLight(byte val)
{
    //Look for value in lookup table
    light_val = val;
    
    //Set light
    analogWrite(LED_PIN, light_val);    
    
}

//Map the light to CIEL lookup table based on the maximum size
void updateLight(byte val, byte maximum)
{
    //Look for value in lookup table
    light_val = CIELPWM(map(val,0,maximum,0,sizeof(CIEL8)-1));
    
    //Set light
    analogWrite(LED_PIN, light_val);    

}


//Blocking fadeUp function
void fadeUp(int speed)  { 

  //Loop all the values in the lookup table
  for (int i=0; i < sizeof(CIEL8); i++)
  {
    //Step thru the lookup table
    light_val = CIELPWM(i);

    // set the brightness of pin 9:
    analogWrite(LED_PIN, light_val);    

    //Wait
    delay(speed);
  }               
}

//Blocking fadeUp function
void fadeDown(int speed)  { 

  //Loop all the values in the lookup table
  for (int i=sizeof(CIEL8)-1; i >= 0; i--)
  {
    //Step thru the lookup table
    light_val = CIELPWM(i);

    // set the brightness of pin 9:
    analogWrite(LED_PIN, light_val);    

    //Wait
    delay(speed);
  }
}