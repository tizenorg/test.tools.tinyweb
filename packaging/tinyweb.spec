Name:		tinyweb 
Summary:	A web service application used for web tests
Version:	1.0.0
release:	0
Url:		https://github.com/testkit/tinyweb
Group:		Development/Testing
License:	GPL-2.0
source:		%{name}-%{version}.tar.gz
source1001:	%{name}.manifest
Requires:	libopenssl-devel

%description 
Web server that provides test resources for web TCs


%prep 
%setup -q 
cp %{SOURCE1001} .


%build
make %{?_smp_mflags}


%install 
install -d %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_datadir}/%{name}
install -m 0755 %{name} %{buildroot}/%{_bindir}
install -m 0755 cgi-getcookie %{buildroot}/%{_bindir}
install -m 0755 cgi-getfield %{buildroot}/%{_bindir}
install -m 0644 server.pem %{buildroot}/%{_datadir}/%{name}


%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_bindir}/cgi-getcookie
%{_bindir}/cgi-getfield
%{_datadir}/%{name}
