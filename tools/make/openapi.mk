JAVA ?= java

OPENAPI_JAR ?= openapi-generator-cli-5.0.0-beta.jar
OPENAPI_JAR_URL ?= https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/5.0.0-beta/$(OPENAPI_JAR)

OPENAPI_CLI ?= $(JAVA) -jar $(PROJECT_ROOT)/bin/$(OPENAPI_JAR)