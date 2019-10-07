# digital.forge.keeper.http.server

This project includes a Python/Flask HTTP server for managing the forge
installation.

This project is under active development.

## Prerequisites

* Java 8 or later must be installed.
* The latest openapi-generator .jar file must be downloaded.
* Python 3.x must be installed with the following packages:
    * `connexion>=2.0.2`
    * `python_dateutil>=2.6.0`

For development on a local machine, CORS must be enabled. This requires the
additional package `flask-cors>=3.0.8`

## Building

Currently, the build is manually invoked via running the openapi-generator. Run
the following command in the project's main folder:

```
java -jar /path/to/openapi-generator.jar generate -i /path/to/api.json -c config/cfg.json -t config/templates -o python -g python-flask
```

**Edits then must be made to the server code to return the expected contents.**

## Running

Currently, the server is run manually using a Python interpreter. Run the
following command in the project's `python` folder:

```
python -m digital.forge.keeper.http.server
```