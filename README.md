# forge-keeper
Utilities and APIs for monitoring the digital forge.

## Development Requirements

* [Python 3](https://www.python.org/downloads/)
* [poetry](https://python-poetry.org/)
* [GNU Make](https://www.gnu.org/software/make/)
* [Java 1.8+](https://www.oracle.com/sa/java/technologies/javase-downloads.html)

### Required Setup

* Update your poetry configuration to put virtual environments in the project
  directory. This is both convenient and not a problem for git to handle.
* Download the OpenAPI .jar file to the bin folder.

For your convenience, you can do this by running the following commands in this
directory:

```
make dev-dependencies
```

## Organization

### bin
Binaries and utilities that are present in source control directories that are
used in the build, test, or publish process but are not distributed.

### src
We're gonna need some source files. Lots of source files.