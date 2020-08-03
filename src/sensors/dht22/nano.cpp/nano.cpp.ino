#include <SimpleDHT.h>

/**
 * This code is deployed to an Arduino device with an attached temperature/humidity
 * sensor. Output is periodic over the serial connection in the format:
 * 
 *   ##.##,##.##
 *   |    |    |
 *    temp humi
 *     *C   %RH
 * 
 * Hardware Setup:
 * Board:  Arduino Nano
 * Sensor: DHT22
 * Connections:
 *   VCC  -> 3V (or 5V)
 *   GND  -> GND
 *   Data -> 2
 */
int data_pin = 2;
SimpleDHT22 device(data_pin);
unsigned long rate = 60 * 1000L; // 1 data point every 60 seconds.

void setup() {
    long speed = 9600L; // Preferred baud rate per community.
    Serial.begin(speed);
}

void loop() {
    float temperature = 0.0;
    float humidity = 0.0;
    
    int err = device.read2(&temperature, &humidity, NULL);
    if (err == SimpleDHTErrSuccess) {
        Serial.print((float) temperature);
        Serial.print(",");
        Serial.println((float) humidity);
    } else {
        Serial.print("Error: ");
        Serial.println(err);
    }

    delay(rate);
}
