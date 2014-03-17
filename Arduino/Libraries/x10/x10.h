/*
 	x10.h - - X10 transmission library for Arduino - Version 0.4
  
  Original library		(0.1) by Tom Igoe.
  Timing bug fixes		(0.2) "   "   "

	Sends X10 commands.

*/

// ensure this library description is only included once
#ifndef x10_h
#define x10_h

// include types & constants of Wiring core API
#include <stdlib.h>

#if (ARDUINO >= 100)
#include <Arduino.h>
#else
#include <WProgram.h>
#endif

#include "pins_arduino.h"

// library interface description
class x10 {
  public:
	// constructors:
	x10(uint8_t zeroCrossingPin, uint8_t dataPin);
	// write command method:
	void write(byte houseCode, byte numberCode, byte numRepeats);
	// returns the version number:
	int version(void);

  private:
	volatile uint8_t *zeroCrossingReg;	// AC zero crossing pin
	uint8_t zeroCrossingBit;
  	uint8_t dataPin;			// data out pin
  	// sends the individual bits of the commands:
	void sendBits(byte cmd, byte numBits, byte isStartCode);
	// checks for AC zero crossing
	void waitForZeroCross(void);
};

#endif

