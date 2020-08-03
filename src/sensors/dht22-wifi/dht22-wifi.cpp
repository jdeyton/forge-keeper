#include <Arduino.h>
//#include <SPI.h>
//#include <WiFiNINA.h>

//const boolean DEBUG = true;
//const byte MAX_MESSAGE_SIZE = 100;
//char message[MAX_MESSAGE_SIZE];

/**************************************
 * REQUIRED SETUP AND LOOP OPERATIONS *
 **************************************/
void setup() {
    long speed = 9600L; // Preferred baud rate per community.
    Serial.begin(speed);
    while (!Serial); // Wait for serial port to connect.
}

void loop() {
	Serial.println("foo");
//	delay(1000);
}
/**********************
 * SUPPLEMENTAL LOGIC *
 **********************/

/**
 * If DEBUG is turned on, this will print an input message over serial. The
 * trailing newline must be included in the message.
 */
void log(const char* message) {
//	if (DEBUG) {
//		Serial.print(message);
//	}
}


