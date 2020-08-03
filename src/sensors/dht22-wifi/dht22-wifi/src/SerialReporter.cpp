#include "SerialReporter.h"

SerialReporter::SerialReporter() {
    Serial.begin(BAUD_RATE);
    // Wait for serial port to connect.
    while (!Serial);
}

boolean SerialReporter::report(const char* message) {
    Serial.print(message);
    return true;
}

boolean SerialReporter::report(const Printable* p) {
    Serial.println(*p);
    return true;
}
