PKG_NAME := jdk-commons-logging
URL := https://repo1.maven.org/maven2/commons-logging/commons-logging/1.2/commons-logging-1.2.jar
ARCHIVES := https://repo1.maven.org/maven2/commons-logging/commons-logging/1.2/commons-logging-1.2.pom %{buildroot}

include ../common/Makefile.common
