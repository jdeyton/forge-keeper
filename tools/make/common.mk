# Allow these Python defines to be provided in advance.

# Make "all" the default target.
all:

# Declare clean.
clean:

# Both should be evaluated regardless..
.PHONY: all clean

# System commands:
CP ?= /bin/cp -f
CURL ?= /bin/curl
MV ?= /bin/mv -f
RM ?= /bin/rm -f
RMDIR ?= /bin/rmdir
TOUCH ?= /bin/touch

# Other commands:
JAVA ?= java
