PROJECT_ROOT ?= $(shell git rev-parse --show-toplevel)
include $(PROJECT_ROOT)/tools/make/common.mk

OPENAPI_JAR ?= openapi-generator-cli-5.0.0-beta.jar
OPENAPI_JAR_URL ?= https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/5.0.0-beta/$(OPENAPI_JAR)

# ---- The OpenAPI generator jar file ---- #
# The jar file itself:
$(OPENAPI_JAR):
	$(CURL) -O $(OPENAPI_JAR_URL)
all: $(OPENAPI_JAR)
# Cleanup:
clean-$(OPENAPI_JAR):
	$(RM) $(OPENAPI_JAR)
.PHONY: clean-$(OPENAPI_JAR)
clean: clean-$(OPENAPI_JAR)
	