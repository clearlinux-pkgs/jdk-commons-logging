Name     : jdk-commons-logging
Version  : 1.2
Release  : 3
URL      : https://repo1.maven.org/maven2/commons-logging/commons-logging/1.2/commons-logging-1.2.jar
Source0  : https://repo1.maven.org/maven2/commons-logging/commons-logging/1.2/commons-logging-1.2.jar
Source1  : https://repo1.maven.org/maven2/commons-logging/commons-logging/1.2/commons-logging-1.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-commons-logging-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-commons-logging package.
Group: Data

%description data
data components for the jdk-commons-logging package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/commons-logging.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/commons-logging.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/commons-logging.xml \
%{buildroot}/usr/share/maven-poms/commons-logging.pom \
%{buildroot}/usr/share/java/commons-logging.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/commons-logging.jar
/usr/share/maven-metadata/commons-logging.xml
/usr/share/maven-poms/commons-logging.pom
