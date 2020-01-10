%global debug_package   %{nil}
%global import_path     github.com/coreos/go-systemd
%global gopath          %{_datadir}/gocode
%global commit          9d69345e9a0dee51b8ebabb86b7b505db9851461
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-coreos-go-systemd
Version:        0
Release:        0.4.git%{shortcommit}%{?dist}
Summary:        Go bindings to systemd socket activation, journal and D-BUS APIs
License:        ASL 2.0
URL:            http://%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/go-systemd-%{shortcommit}.tar.gz
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel
Requires:       golang
Summary:        Go bindings to systemd socket activation, journal and D-BUS APIs
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/activation) = %{version}-%{release}
Provides:       golang(%{import_path}/dbus) = %{version}-%{release}
Provides:       golang(%{import_path}/journal) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for building other packages
which use coreos/go-systemd.

%prep
%setup -n go-systemd-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/{activation,dbus,journal}
cp -av {activation,dbus,journal} %{buildroot}/%{gopath}/src/%{import_path}

%files devel
%doc LICENSE README.md
%dir %attr(755,root,root) %{gopath}
%dir %attr(755,root,root) %{gopath}/src
%dir %attr(755,root,root) %{gopath}/src/github.com
%dir %attr(755,root,root) %{gopath}/src/github.com/coreos
%dir %attr(755,root,root) %{gopath}/src/%{import_path}
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/activation
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/dbus
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/journal
%{gopath}/src/%{import_path}/activation/*.go
%{gopath}/src/%{import_path}/dbus/*.go
%{gopath}/src/%{import_path}/journal/*.go

%changelog
* Mon Mar 31 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.4.git
- upgrade to latest version

* Fri Oct 18 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.3.git68bc612
- double quotes removed from provides

* Mon Oct 14 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.2.git68bc612
- provides golang("github.com/coreos/go-systemd")
- defattr removed

* Sat Oct 12 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.1.git68bc612
- Initial fedora package
