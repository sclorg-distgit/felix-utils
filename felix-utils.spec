%{?scl:%scl_package felix-utils}
%{!?scl:%global pkg_name %{name}}

%global bundle org.apache.felix.utils

Name:           %{?scl_prefix}felix-utils
Version:        1.10.0
Release:        1.1%{?dist}
Summary:        Utility classes for OSGi
License:        ASL 2.0
URL:            http://felix.apache.org
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/felix/%{bundle}/%{version}/%{bundle}-%{version}-source-release.tar.gz

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.osgi:org.osgi.compendium)
BuildRequires:  %{?scl_prefix}mvn(org.osgi:org.osgi.core)

%description
Utility classes for OSGi

%package javadoc
Summary:          API documentation for %{pkg_name}

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -q -n %{bundle}-%{version}

%pom_remove_plugin :apache-rat-plugin

%mvn_file :%{bundle} "felix/%{bundle}"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE
%doc DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 1.10.0-1.1
- Automated package import and SCL-ization

* Fri Jun 02 2017 Roman Vais <rvais@redhat.com> - 1.10.0-1
- Update to upstream version 1.10.0

* Wed Mar 29 2017 Michael Simacek <msimacek@redhat.com> - 1.9.0-1
- Update to upstream version 1.9.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Michael Simacek <msimacek@redhat.com> - 1.8.6-1
- Update to upstream version 1.8.6

* Thu Oct 13 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.2-4
- Remove build-dependency on maven-source-plugin

* Thu Jun 16 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.2-3
- Regenerate build-requires
- Update to current packaging guidelines

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Michael Simacek <msimacek@redhat.com> - 1.8.2-1
- Update to upstream version 1.8.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 12 2015 Michael Simacek <msimacek@redhat.com> - 1.8.0-1
- Update to upstream version 1.8.0

* Tue Jan 27 2015 Michael Simacek <msimacek@redhat.com> - 1.6.0-1
- Update to upstream version 1.6.0

* Tue Jan 27 2015 Mat Booth <mat.booth@redhat.com> - 1.4.0-1
- Update to upstream 1.4.0 release
- Re-enable tests

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-8
- Add build-requires on mockito

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Michal Srb <msrb@redhat.com> - 1.2.0-6
- Update BR

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-5
- Remove BuildRequires on maven-surefire-provider-junit4

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2.0-4
- Use Requires: java-headless rebuild (#1067528)

* Mon Aug 05 2013 Mat Booth <fedora@matbooth.co.uk> - 1.2.0-3
- Update for latest guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 17 2013 Mat Booth <fedora@matbooth.co.uk> - 1.2.0-1
- Update to latest upstream version rhbz #892553.
- Drop patch, use preferred %%pom_* macros instead.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1.0-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 03 2013 Jaromir Capik <jcapik@redhat.com> - 1.1.0-7
- Changing target from jsr14 to 1.5 (#842593)

* Tue Sep  4 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.0-6
- Install NOTICE with javadoc pakcage

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 13 2011 Jaromir Capik <jcapik@redhat.com> - 1.1.0-3
- osgi.org groupId patch removed (fixed in felix-osgi-* packages)

* Thu Sep 08 2011 Jaromir Capik <jcapik@redhat.com> - 1.1.0-2
- Moved to felix subdir
- Minor spec file changes

* Wed Jul 13 2011 Jaromir Capik <jcapik@redhat.com> - 1.1.0-1
- Initial version
