Summary:	CUPS backend wrapper which can capture print datas before they are sent to a printer and process
Summary(pl.UTF-8):	Sterownik CUPS pozwalający przechwycić zadanie i przetworzyć
Name:		tea4cups
Version:	3.12
Release:	1
License:	GPL v2
Group:		Applications/Printing
# NOTE: from svn:
# svn co http://svn.pykota.com/tea4cups/tags/3.12/
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	5c3b832d1bbbc1495bf2e47acc7b12eb
URL:		http://www.pykota.com/software/tea4cups
BuildRequires:	cups-devel
BuildRequires:	rpm-pythonprov
Requires:	cups >= 1:1.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	%(cups-config --serverroot 2>/dev/null)
%define		_libdir		%(cups-config --serverbin 2>/dev/null)

%description
Tea4CUPS is a CUPS backend wrapper which can capture print datas
before they are sent to a printer and process, duplicate or dispatch
them in a number of ways.

%description -l pl.UTF-8
Sterownik CUPS pozwalający przechwycić zadanie przed wysłaniem do
drukarki żeby przetworzyć, zduplikować lub przekierować na dowolny
sposób.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir}/backend}
install -p tea4cups $RPM_BUILD_ROOT%{_libdir}/backend/%{name}
cp -a tea4cups.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS README NEWS TODO
%attr(644,lp,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_libdir}/backend/%{name}
