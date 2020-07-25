PROJECT_ROOT ?= $(shell git rev-parse --show-toplevel)
include $(PROJECT_ROOT)/tools/make/common.mk
include $(PROJECT_ROOT)/tools/make/openapi.mk

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
	