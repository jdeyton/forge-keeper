/**
 * This source is deployed to an Arduino with an attached temperature/humidity
 * sensor. Output is periodic in the format:
 * 
 * ##.##,##.##
 * |    |    |
 *  temp humi
 *   *C   %RH
 * 
 * ==== Hardware Setup ====
 * Board        => Arduino NANO, Arduino NANO 33 IoT
 * Sensor       => DHT22 (3-pin)
 * Connections  =>
 *      VCC  -> 3.3V
 *      GND  -> GND
 *      Data -> 2 (digital)
 */
#include <Arduino.h>

#include "Monitor.h"
#include "Network.h"
#include "Reporter.h"
#include "SerialReporter.h"

const boolean DEBUG = true;
const byte MAX_MESSAGE_SIZE = 100;
char message[MAX_MESSAGE_SIZE];
unsigned long rate = 60 * 1000L; // 1 data point every 60 seconds.

Monitor* monitor;
Reporter* reporter;

void log(const char* message);
void log_connection_info();
int stringify_ip(const IPAddress ip, char* buffer);
int stringify_mac(const byte* mac, char* buffer);

/**************************
 *          MAIN          *
 **************************/
void setup() {
    monitor = new Monitor(2);           // Listen on (digital) data pin 2.
    reporter = new SerialReporter();    // Output on serial connection.
    
    log("Connecting to network...\n");
    Network network;
    if (!network.connect()) {
        log("Connection failed.\n");
        while (1); // Stop booting.
    }
    log_connection_info();
}

void loop() {
    if (monitor->poll()) {
        reporter->report(monitor);
    } else {
        log("Error polling temperature/humidity");
    }

    delay(rate);
}

/**************************
 *      OPERATIONS        *
 **************************/

/**
 * Prints a message to serial output if debugging is enabled. Does not include a
 * trailing newline.
 * 
 * @param message The message to print. Newlines must be manually inserted.
 */
void log(const char* message) {
    if (DEBUG) {
        Serial.print(message);
    }
}

/**
 * Determines and logs the current wifi connection details.
 */
void log_connection_info() {
    byte mac[6];
    IPAddress ip;
    char ip_string[16];
    char mac_string[18];
    
    WiFi.macAddress(mac);
    stringify_mac(mac, mac_string);
    snprintf(message, MAX_MESSAGE_SIZE, "HWADDR: %s\n", mac_string);
    log(message);
    
    ip = WiFi.localIP();
    stringify_ip(WiFi.localIP(), ip_string);
    snprintf(message, MAX_MESSAGE_SIZE, "IPADDR: %s\n", ip_string);
    log(message);
  
    snprintf(message, MAX_MESSAGE_SIZE, "SSID: %s\n", WiFi.SSID());
    log(message);

    WiFi.BSSID(mac);
    stringify_mac(mac, mac_string);
    snprintf(message, MAX_MESSAGE_SIZE, "GATEWAY HWADDR: %s\n", mac_string);
    log(message);

    stringify_ip(WiFi.gatewayIP(), ip_string);
    snprintf(message, MAX_MESSAGE_SIZE, "GATEWAY IPADDR: %s\n", ip_string);
    log(message);
    
    stringify_ip(WiFi.subnetMask(), ip_string);
    snprintf(message, MAX_MESSAGE_SIZE, "NETMASK: %s\n", ip_string);
    log(message);
}

/**
 * Converts an IPAddress into a C-style string.
 * 
 * @param ip The IPAddress to convert.
 * @param buffer The shared buffer for writing small-ish strings.
 * @returns The result of the underlying snprintf.
 */
int stringify_ip(const IPAddress ip, char* buffer) {
    return snprintf(buffer, 16, "%u.%u.%u.%u", ip[0], ip[1], ip[2], ip[3]);
}

/**
 * Converts a MAC address into a C-style string.
 * 
 * @param mac The MAC address to convert.
 * @param buffer The shared buffer for writing small-ish strings.
 * @returns The result of the underlying snprintf.
 */
int stringify_mac(const byte* mac, char* buffer) {
    return snprintf(buffer, 18, "%02X:%02X:%02X:%02X:%02X:%02X", mac[5], mac[4], mac[3], mac[2], mac[1], mac[0]);
}