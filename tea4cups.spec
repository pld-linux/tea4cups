Summary:	Tea4CUPS is the Swiss Army's knife of the CUPS Administrator
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
BuildRequires:	sed >= 4.0
Requires:	cups >= 1:1.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	%(cups-config --serverroot 2>/dev/null)
%define		_libdir		%(cups-config --serverbin 2>/dev/null)

%description
Tea4CUPS is a CUPS backend wrapper which can capture print data before
it is sent to a printer and process, duplicate or dispatch it in a
number of ways.

%description -l pl.UTF-8
Sterownik CUPS pozwalający przechwycić zadanie przed wysłaniem do
drukarki żeby przetworzyć, zduplikować lub przekierować na dowolny
sposób.

%prep
%setup -q
%{__sed} -i -e '1s,#!.*python,#!%{__python},' %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir}/backend}
install -p %{name} $RPM_BUILD_ROOT%{_libdir}/backend/%{name}
cp -a %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS README NEWS TODO
%attr(644,lp,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_libdir}/backend/%{name}
