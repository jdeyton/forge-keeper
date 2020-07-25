OPENAPI_JAR ?= openapi-generator-cli-5.0.0-beta.jar
OPENAPI_JAR_URL ?= https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/5.0.0-beta/$(OPENAPI_JAR)

all: $(OPENAPI_JAR)

.PHONY: all clean

$(OPENAPI_JAR):
	curl -O $(OPENAPI_JAR_URL)

clean:
	$(RM) -f $(OPENAPI_JAR)
	