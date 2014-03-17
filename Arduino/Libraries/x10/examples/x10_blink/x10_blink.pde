/*  X10 blink

  Blinks an lamp on an X10 lamp module, set to Unit 1, House A
  Example was built using a PL513
  Also tested using a PSC04 unit
  X10 One-Way Interface Module from http://www.smarthome.com 
  as the modem, and a Powerhouse X10 Lamp Module from Smarthome
  to plug the lamp in.
  
  created 15 June 2007 by Tom Igoe
  modified July 2010 by Paul Stoffregen <paul@pjrc.com>
*/
#include <x10.h>
#include <x10constants.h>

const int zeroCrossPin = 2;
const int dataPin      = 3;

// set up a new x10 instance:
x10 myHouse =  x10(zeroCrossPin, dataPin);

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Lights on:");
  myHouse.write(A, UNIT_1, 3);
  myHouse.write(A, ON, 3);
  delay(1000);

  Serial.println("Lights off:");
  myHouse.write(A, UNIT_1, 3);
  myHouse.write(A, OFF, 3);
  delay(1000);
}
