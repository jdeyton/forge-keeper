#ifndef NETWORK_H
#define NETWORK_H

#include <WiFiNINA.h>

/**
 * @brief A wrapper for network connections.
 * @detailed
 * 
 * This class provides a simple wrapper around a WiFiNINA-based network
 * connection. Currently, the only use is establishing the connection.
 */
class Network {
    private:
        static const char* SSID;
        static const char* KEY;

    public:
        /**
         * @brief Construct a new Network object.
         */
        Network();

        /**
         * @brief Connects to the network.
         * 
         * @return boolean True if the connection was established, false
         * otherwise.
         */
        boolean connect();
};

#endif