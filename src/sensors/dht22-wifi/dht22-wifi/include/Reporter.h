#ifndef REPORTER_H
#define REPORTER_H

#include <Arduino.h>
#include <Printable.h>

/**
 * @brief An interface for a data reporter.
 * @detailed
 * 
 * Implementations of this interface are responsible for all logic necessary to
 * communicate a message to a recipient, be it the local Serial connection or a
 * remote server.
 * 
 */
class Reporter {
    private:

    public:
        /**
         * @brief Report a data point to the listener.
         * 
         * @param message The string to print.
         * @return boolean True if successfully reported, false otherwise.
         */
        virtual boolean report(const char* message);

        /**
         * @brief Report a printable data point to the listener.
         * 
         * @param p A printable (i.e., stringifiable) object.
         * @return boolean True if successfully reported, false otherwise.
         */
        virtual boolean report(const Printable* p);
};

#endif