Summary:	Program for demonstrating the unsafeness of TCP
Summary(pl):	Program do nas³uchu po³±czeñ TCP/UDP/ICMP
Name:		sniffit
Version:	0.3.7
Release:	2
Copyright:	Free
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Source:		http://reptile.rug.ac.be/~coder/sniffit/files/%{name}.%{version}.beta.tar.gz 
Patch:		sniffit-fixes.patch
URL:		http://reptile.rug.ac.be/~coder/sniffit/sniffit.html
Buildrequires:	ncurses-devel >= 5.0
Buildrequires:	libpcap-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Sniffit is a packet sniffer for TCP/UDP/ICMP packets. Sniffit is able to
give you very detailed technical info on these packets (SEQ, ACK, TTL,
Window, ...) but also packet contence in different formats (hex or plain
text, ...).

%description -l pl
Sniffit jest programem do pods³uchu pakietów TCP/UDP/ICMP. Sniffit jest w stanie
podaæ Ci bardzo wiele informacji o tych pakietach (SEQ, ACK, TTL, Okno, ...)
a tak¿e ich zawarto¶æ w ró¿nych formatach (szesnastkowo lub w czystej postaci,
...).

%prep
%setup -q -n %{name}.%{version}.beta
%patch -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{5,8}}

install -s sniffit $RPM_BUILD_ROOT%{_bindir}

install sniffit.5 $RPM_BUILD_ROOT%{_mandir}/man5
install sniffit.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man?/* \
	PLUGIN-HOWTO README.FIRST BETA-TESTING \
	HISTORY sample_config_file sniffit-FAQ

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
