%{?_javapackages_macros:%_javapackages_macros}
%global base_name       modeler
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          2.0.1
Release:          13.0%{?dist}
Summary:          Model MBeans utility classes
License:          ASL 2.0
URL:              http://commons.apache.org/%{base_name}/
Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
# POM file based on the one from an unreleased upstream snapstream
Source1:          pom.xml
BuildArch:        noarch

BuildRequires:    java-devel >= 1:1.6.0
BuildRequires:    jpackage-utils
BuildRequires:    ant
BuildRequires:    apache-commons-beanutils
BuildRequires:    apache-commons-digester
BuildRequires:    apache-commons-logging
BuildRequires:    maven-local


%description
Commons Modeler makes the process of setting up JMX (Java Management
Extensions) MBeans easier by configuring the required meta data using an XML
descriptor. In addition, Modeler provides a factory mechanism to create the
actual Model MBean instances.

%package javadoc
Summary:          Javadoc for %{name}

Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' RELEASE-NOTES.txt
sed -i 's/\r//' NOTICE.txt

# Copy pom file into place
cp -p %{SOURCE1} .

# Remove redundant dep on mx4j
%pom_remove_dep mx4j:mx4j-jmx

# Fix ant dependency
%pom_remove_dep ant:ant
%pom_add_dep org.apache.ant:ant:1.8

%mvn_alias : org.apache.commons:%{short_name}
%mvn_file : %{name} %{short_name}

%build
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Thu Aug  8 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0.1-13
- Update to latest packaging guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Mat Booth <fedora@matbooth.co.uk> - 2.0.1-11
- Package pom.xml and build with maven, rhbz #825455
- Remove ancient obsoletes/provides for jakarta package
- Fix some misc other outdated packaging practices

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 2 2010 Chris Spike <chris.spike@arcor.de> 2.0.1-6
- Rename and rebase from jakarta-commons-modeler
