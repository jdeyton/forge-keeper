#include <avr/dtostrf.h>

#include "Monitor.h"

Monitor::Monitor(const int pin): device(pin) {
    humidity = 0.0;
    temperature = 0.0;
}

boolean Monitor::poll() {
    int err = device.read2(&temperature, &humidity, NULL);
    if (err == SimpleDHTErrSuccess) {
        temperature = constrain(temperature, 0.0, 99.99);
        humidity = constrain(humidity, 0.0, 99.99);
        return true;
    }
    return false;
}

float Monitor::getHumidity() const {
    return humidity;
}

float Monitor::getTemperature() const {
    return temperature;
}

size_t Monitor::printTo(Print& p) const {
    char buffer[12];
    char temperature_buffer[6]; // max string width: ##.## => 6
    char humidity_buffer[6];    // max string width: ##.## => 6
    dtostrf(temperature, 0, 2, temperature_buffer);
    dtostrf(humidity, 0, 2, humidity_buffer);
    snprintf(buffer, 12, "%s,%s", temperature_buffer, humidity_buffer);
    p.print(buffer);
    return strlen(buffer);
}

