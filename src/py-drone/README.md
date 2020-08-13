# py-drone

This project provides a python client (drone) that feeds data to the forge-keeper using the provided API client classes.

The current intention is for this client to read sensor data off a serial port, authenticate with the web service, and send the data for long-term storage in the backend database.

## How to Deploy

### Configuration

Create a `py-drone.conf` JSON file containing a single object with
the below nested properties/objects:

* **port:** The serial port, e.g., `/dev/tty(ACM|S|USB)[0-3]`.
* **rate:** The modulating rate (bauds), commonly `9600`. This must match the
  value used by the attached sensor.
* **drone:** The UUID string of the drone whose data is being reported.
* **archives:** A JSON array of UUID strings for archives where data will be
  sent. If multiple UUIDs are specified, then the process will try to read each
  value out of the comma-separated output of the sensor on the serial port.
* **url:** (optional) The URL to which data will be sent. If not specified, a
  default is used from the API library.

### Build and Deploy

Create the following secrets as necessary:

- **forge-drone-conf:** Your `py-drone.conf` contents.
- **forge-keeper-https-cert:** Your server's (self-signed) SSL cert.

Go to the `docker` directory and do the following:

- Create `pip.conf` with the necessary info to read packages from your PyPI.
- Run `docker build --network=host -t forge-drone .`
- Run `docker stack deploy -c drone.yml forge-drone`