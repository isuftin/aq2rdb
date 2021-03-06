Name:           aq2rdb-client
Version:        1.2.0
Release:        1
Summary:        A command-line program to call the aq2rdb Web service.
Packager:       Andrew Halper <ashalper@usgs.gov>
Vendor:         USGS Office of Water Information
Group:          Applications/Internet
BuildArch:      noarch
Source0:        https://github.com/ashalper-usgs/aq2rdb/%{name}-%{version}.tar.gz
License:        USGS
URL:            https://github.com/ashalper-usgs/aq2rdb
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
Prefix:         /usr/local

%description
The aq2rdb client is a command-line program intended to replace the
NWIS program nwts2rdb. The client calls the aq2rdb Web service to
produce RDB files on standard output.

%prep
%setup -q

%build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{prefix}/bin
# only one file in the package
cp aq2rdb ${RPM_BUILD_ROOT}%{prefix}/bin
chmod 755 aq2rdb ${RPM_BUILD_ROOT}%{prefix}/bin/aq2rdb

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%attr(755,root,root) %{prefix}/bin/aq2rdb
%doc

%changelog

* Wed Apr 27 2016 Andrew Halper <ashalper@usgs.gov> 1.2.0-1
- Added nwts2rdb "-o" option, to save output to a local file.

* Tue Mar 29 2016 Andrew Halper <ashalper@usgs.gov> 1.1.11-2
- Rebuilt on Solaris SPARC because CentOS RPM would not install,
  despite professing to be "noarch".

* Fri Mar 25 2016 Andrew Halper <ashalper@usgs.gov> 1.1.11-1%{?dist}
- Appended newline to final line of usage statement.
- Re-targeted "aq2rdb" Web service reference to cidasdqaasaq2rd.

* Wed Mar 23 2016 Andrew Halper <ashalper@usgs.gov> 1.1.10-2%{?dist}
- Some minor clean-up of .spec file.

* Wed Mar 23 2016 Andrew Halper <ashalper@usgs.gov> 1.1.10-1%{?dist}
- Initial release.
