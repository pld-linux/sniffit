Summary:	Program for demonstrating the unsafeness of TCP
Summary(pl):	Program do nas�uchu po��cze� TCP/UDP/ICMP
Name:		sniffit
Version:	0.3.7
Release:	5
License:	Free
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narz�dzia
Group(pt_BR):	Rede/Utilit�rios
Source0:	http://reptile.rug.ac.be/~coder/sniffit/files/%{name}.%{version}.beta.tar.gz
Patch0:		%{name}-fixes.patch
URL:		http://reptile.rug.ac.be/~coder/sniffit/sniffit.html
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	libpcap-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sniffit is a packet sniffer for TCP/UDP/ICMP packets. Sniffit is able
to give you very detailed technical info on these packets (SEQ, ACK,
TTL, Window, ...) but also packet contence in different formats (hex
or plain text, ...).

%description -l pl
Sniffit jest programem do pods�uchu pakiet�w TCP/UDP/ICMP. Sniffit
jest w stanie poda� Ci bardzo wiele informacji o tych pakietach (SEQ,
ACK, TTL, Okno, ...) a tak�e ich zawarto�� w r�nych formatach
(szesnastkowo lub w czystej postaci, ...).

%prep
%setup -q -n %{name}.%{version}.beta
%patch -p1

%build
cd libpcap
	aclocal
	autoconf
cd ..
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{5,8}}

install sniffit $RPM_BUILD_ROOT%{_bindir}

install sniffit.5 $RPM_BUILD_ROOT%{_mandir}/man5
install sniffit.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf PLUGIN-HOWTO README.FIRST BETA-TESTING \
	HISTORY sample_config_file sniffit-FAQ

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
