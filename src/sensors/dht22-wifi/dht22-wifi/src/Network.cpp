#include "Network.h"
#include <WiFiNINA.h>

const char* Network::SSID = "arcturus";
const char* Network::KEY  = "You shall not pass!!!";

Network::Network() {
    // Nothing to do yet.
}

boolean Network::connect() {
    if (WiFi.status() == WL_NO_MODULE) {
        return false;
    }

    int status = WL_IDLE_STATUS;
    while (status != WL_CONNECTED) {
        status = WiFi.begin(SSID, KEY);
        delay(10000);
    }
    return true;
}