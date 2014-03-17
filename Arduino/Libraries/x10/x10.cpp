/*
  x10.cpp - X10 transmission library for Arduino version 0.4
  
  Original library		(0.1) by Tom Igoe.
  Timing bug fixes		(0.2) "   "   "
  #include bug fixes for 0012	(0.3) "   "   "
  use pullup, minor tweaks	(0.4) Paul Stoffregen <paul@pjrc.com>
    
  Zero crossing algorithms borrowed from David Mellis' shiftOut command
  for Arduino.
  
  The circuits can be found at 
    http://www.arduino.cc/en/Tutorial/x10
 */

#include <stdlib.h>

#if (ARDUINO >= 100)
#include <Arduino.h>
#else
#include <WProgram.h>
#endif

#include "x10.h"
#include "x10constants.h"

/*
 Constructor.
 
 Sets the pins and sets their I/O modes.
 
 */
x10::x10(uint8_t zeroCrossingPin, uint8_t dataPin)
{
	this->dataPin = dataPin;		// the output data pin
	zeroCrossingReg = portInputRegister(digitalPinToPort(zeroCrossingPin));
	zeroCrossingBit = digitalPinToBitMask(zeroCrossingPin);
  
	// Set I/O modes:
	#ifdef INPUT_PULLUP
	pinMode(zeroCrossingPin, INPUT_PULLUP);
	#else
	pinMode(zeroCrossingPin, INPUT);
	digitalWrite(zeroCrossingPin, HIGH);
	#endif
	pinMode(dataPin, OUTPUT);
}



/*
	Writes an X10 command out to the X10 modem
*/
void x10::write(byte houseCode, byte numberCode, byte numRepeats)
{
	byte startCode = B1110; 	// every X10 command starts with this

	// repeat as many times as requested:
 	for (uint8_t i = 0; i < numRepeats; i++) {
		// send the three parts of the command:
 		sendBits(startCode, 4, true);	
  		sendBits(houseCode, 4, false);
  		sendBits(numberCode, 5, false);
  	}
  	// if this isn't a bright or dim command, it should be followed by
  	// a delay of 3 power cycles (or 6 zero crossings):
  	if ((numberCode != BRIGHT) && (numberCode != DIM)) {
 		for (uint8_t i = 0; i < 6; i++) {
  			waitForZeroCross();
		}
  	}
}

/*
	Writes a sequence of bits out.  If the sequence is not a start code,
	it repeats the bits, inverting them.
*/
void x10::sendBits(byte cmd, byte numBits, byte isStartCode) {
	byte thisBit;	// copy of command so we can shift bits
  
	// iterate the number of bits to be shifted:
	for (uint8_t i=1; i<=numBits; i++) {
		// wait for a zero crossing change:
		waitForZeroCross();
		// shift off the last bit of the command:
		thisBit = !!(cmd & (1 << (numBits - i)));
		
		// repeat once for each phase:
		for (uint8_t phase = 0; phase < 3; phase++) {
			// set the data Pin:
			digitalWrite(this->dataPin, thisBit);
			delayMicroseconds(BIT_LENGTH);
			// clear the data pin:
			digitalWrite(this->dataPin, LOW);
			delayMicroseconds(BIT_DELAY);
		}
		
		// if this command is a start code, don't
		// send its complement.  Otherwise do:
		if(!isStartCode) {
			// wait for zero crossing:
			waitForZeroCross();
			for (uint8_t phase = 0; phase < 3; phase++) {
				// set the data pin:
				digitalWrite(this->dataPin, !thisBit);
				delayMicroseconds(BIT_LENGTH);
				// clear the data pin:
				digitalWrite(dataPin, LOW);
				delayMicroseconds(BIT_DELAY);
			}
		}
	}
}


/*
  waits for a the zero crossing pin to cross zero

*/
//void x10::waitForZeroCross(uint8_t howManyTimes)
void x10::waitForZeroCross(void)
{
	// wait for pin to change:
	if (*zeroCrossingReg & zeroCrossingBit) {
		while (*zeroCrossingReg & zeroCrossingBit) /* wait */ ;
	} else {
		while (!(*zeroCrossingReg & zeroCrossingBit)) /* wait */ ;
	}
}


/*
  version() returns the version of the library:
*/
int x10::version(void)
{
  return 3;
}
