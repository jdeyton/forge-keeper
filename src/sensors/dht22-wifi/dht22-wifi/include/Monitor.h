#ifndef MONITOR_H
#define MONITOR_H

#include <Print.h>
#include <Printable.h>
#include <SimpleDHT.h>

/**
 * @brief A wrapper for SimpleDHT using a DHT22 sensor.
 * @detailed
 * 
 * This class provides a simple wrapper around a DHT22 sensor. The basic use is:
 *   1 - Refresh the data by invoking the "poll" operation.
 *   2 - Query the desired values by calling the getters.
 *   3 - Rinse and repeat.
 * 
 */
class Monitor: public Printable {
    private:
        /**
         * The current relative humidity in %RH.
         */
        float humidity;
        /**
         * The current temperature in degrees C.
         * 
         */
        float temperature;
        /**
         * The underlying SimpleDHT object for reading sensor data.
         */
        SimpleDHT22 device;

    public:

        /**
         * @brief Construct a new Monitor object
         * 
         * @param pin The (digital) data pin to which the sensor is connected.
         */
        Monitor(const int pin);

        /**
         * @brief Pulls new sensor data from the device.
         * 
         * @return boolean True if successful, false otherwise.
         */
        boolean poll();

        /**
         * @brief Get the current humidity (%RH).
         * 
         * @return float The current humidity.
         */
        float getHumidity() const;
        
        /**
         * @brief Get the current temperature (degrees C).
         * 
         * @return float The current temperature.
         */
        float getTemperature() const;

        /**
         * @brief Implementation of Printable. Prints the data in a pre-defined
         * format.
         * 
         * @param p The Print object.
         * @return size_t The length of the printed string, including the null
         * terminator.
         */
        size_t printTo(Print& p) const;
};

#endif