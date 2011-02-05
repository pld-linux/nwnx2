%define 	org_name	linnwnx2
Summary:	Neverwinter Nights Externder
Summary(pl.UTF-8):	Neverwinter Nights Externder - pakiet rozszerzający Neverwinter Nights
Name:		nwnx2
Version:	2.5.3
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://nwnx.org/uploads/media/%{org_name}-%{version}-rc1.tar.gz
# Source0-md5:	515271f9bf8fd6a462de03776f0acc84
URL:		http://nwnx.org/
BuildRequires:	mysql-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NWNX adds extra functionality such as SQL database support, additional
scripting functions, performance monitoring and many other features to
the Neverwinter Nights game.

%description -l pl.UTF-8
NWNX dodaje dodatkową funkcjonalność (taką jak obsługę baz danych SQL,
dodatkowe funkcje skryptowe, monitorowanie wydajności i wiele innych)
do gry Neverwinter Nights.

%prep
%setup -q -n linnwnx2

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

%if 0
# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%endif

# initscript and its config
%if %{with initscript}
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%endif
