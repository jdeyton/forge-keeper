#include <SPI.h>
#include <WiFiNINA.h>

const boolean DEBUG = true;
const byte MAX_MESSAGE_SIZE = 100;
char message[MAX_MESSAGE_SIZE];

// Simple log here that can be turned off.
void log(const char* message) {
    Serial.print(message);
}

boolean connect_to_wifi() {
    char wifi_ssid[] = "arcturus";
    char wifi_key[]  = "You shall not pass!!!";

    if (WiFi.status() == WL_NO_MODULE) {
        log("Communication with WiFi module failed!\n");
        return false;
    }

    /* Not needed after deployment. */
    /*
    String fv = WiFi.firmwareVersion();
    if (fv < WIFI_FIRMWARE_LATEST_VERSION) {
        log("Please upgrade the firmware");
    }
    */

    int status = WL_IDLE_STATUS;
    while (status != WL_CONNECTED) {
        snprintf(message, MAX_MESSAGE_SIZE, "Attempting to connect to SSID: %s\n", wifi_ssid);
        log(message);
        status = WiFi.begin(wifi_ssid, wifi_key);
        delay(10000);
    }
    log("Connected\n");

    if (DEBUG) {
        log_connection_info();
    }

    return true;
}

void setup() {
    long speed = 9600L; // Preferred baud rate per community.
    Serial.begin(speed);
    while (!Serial); // Wait for serial port to connect.

    if (!connect_to_wifi()) {
        log("Connection failed.\n");
        while (1); // Stop booting.
    }
}

void loop() {
  // put your main code here, to run repeatedly:

} 

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

int stringify_ip(const IPAddress ip, char* buffer) {
    return snprintf(buffer, 16, "%u.%u.%u.%u", ip[0], ip[1], ip[2], ip[3]);
}

int stringify_mac(const byte* mac, char* buffer) {
    return snprintf(buffer, 18, "%02X:%02X:%02X:%02X:%02X:%02X", mac[5], mac[4], mac[3], mac[2], mac[1], mac[0]);
}
