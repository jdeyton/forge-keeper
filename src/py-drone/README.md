# py-drone

This project provides a python client (drone) that feeds data to the forge-keeper using the provided API client classes.

The current intention is for this client to read sensor data off a serial port, authenticate with the web service, and send the data for long-term storage in the backend database.

## How to Deploy

### Setup

- Configure poetry to store the virtual environment in the current directory:
  `poetry configure virtualenvs.in-project true`
- Create a virtual environment: `poetry init`
- Ensure the appropriate PyPI is configured in the `pyproject.toml`.
- Add this package: `poetry add digital-forge-drone`

### Configure the Drone

Create `/etc/py-drone.conf` as a JSON file containing a single object with
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

Ensure the file is only readable by the root user.

### Run

```
poetry run py-drone
```