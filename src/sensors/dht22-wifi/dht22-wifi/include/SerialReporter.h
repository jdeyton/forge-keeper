#ifndef SERIAL_REPORTER_H
#define SERIAL_REPORTER_H

#include "Reporter.h"

/**
 * @brief A Reporter implementation that writes to the Serial connection.
 * 
 * This class provides a concrete class that reports data to a Serial
 * connection.
 */
class SerialReporter: public Reporter {
    private:
        /**
         * The baud rate for communication over the serial port. This value is
         * the preferred value based on community discussions.
         */
        const long BAUD_RATE = 9600L;

    public:
        /**
         * @brief Construct a new Serial Reporter object
         */
        SerialReporter();
        
        /**
         * @brief Report a data point over a Serial connection.
         * 
         * @param message The string to print.
         * @return boolean True if successfully reported, false otherwise.
         */
        boolean report(const char* message);

        /**
         * @brief Report a printable data point over a Serial connection.
         * 
         * @param p A printable (i.e., stringifiable) object.
         * @return boolean True if successfully reported, false otherwise.
         */
        boolean report(const Printable* p);
};

#endif