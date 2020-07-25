# forge-keeper
Utilities and APIs for monitoring the digital forge.

## Development Requirements

* [Python 3](https://www.python.org/downloads/)
* [poetry](https://python-poetry.org/)
* [GNU Make](https://www.gnu.org/software/make/)
* [Java 1.8+](https://www.oracle.com/sa/java/technologies/javase-downloads.html)

### Required Setup

By default, poetry likes to put virtual environments in your home directory.
Source control is smart enough to deal with them in the project directories, so
go ahead and apply the following settings:

```
poetry config virtualenvs.in-project true
```

## Organization

### bin
Binaries and utilities that are present in source control directories that are
used in the build, test, or publish process but are not distributed.

### src
We're gonna need some source files. Lots of source files.