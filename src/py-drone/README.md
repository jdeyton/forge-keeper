# py-drone

This project provides a python client (drone) that feeds data to the forge-keeper using the provided API client classes.

The current intention is for this client to read sensor data off a serial port, authenticate with the web service, and send the data for long-term storage in the backend database.

## How to Deploy

This container requires use of serial devices, a feature that is not supported
by Docker Swarm. Thus we must use docker-compose, where secrets also have
limited support.

### Build

Go to the `docker` directory and do the following:

- Create `pip.conf` with the necessary info to read packages from your PyPI.
- Run: `docker build --network=host -t forge-drone .`

### Configure

Create a `/etc/py-drone.conf` JSON file containing a single object with the
below nested properties/objects:

* **port:** The serial port, e.g., `/dev/tty(ACM|S|USB)[0-3]`.
* **rate:** The modulating rate (bauds), commonly `9600`. This must match the
  value used by the attached sensor.
* **drone:** The UUID string of the drone whose data is being reported.
* **archives:** A JSON array of UUID strings for archives where data will be
  sent. If multiple UUIDs are specified, then the process will try to read each
  value out of the comma-separated output of the sensor on the serial port.
* **url:** (optional) The URL to which data will be sent. If not specified, a
  default is used from the API library.

Ensure you have the SSL cert for your server for HTTPS communication at
`/etc/ssl/certs/cert.pem`

### Deploy

```
docker-compose -f drone.yml -p forge-drone up
```