Summary:	Program for demonstrating the unsafeness of TCP
Summary(es):	A network protocol analyzer
Summary(pl):	Program do nas³uchu po³±czeñ TCP/UDP/ICMP
Summary(pt_BR):	Um analisador de protocolos de rede
Name:		sniffit
Version:	0.3.7
Release:	6
Epoch:		1
License:	distributable
Group:		Networking/Utilities
Source0:	http://reptile.rug.ac.be/~coder/sniffit/files/%{name}.%{version}.beta.tar.gz
# Source0-md5:	2697cc18878480199fe6db1e61134d5a
Patch0:		%{name}-fixes.patch
Patch1:		%{name}-gcc33.patch
URL:		http://reptile.rug.ac.be/~coder/sniffit/sniffit.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sniffit is a packet sniffer for TCP/UDP/ICMP packets. Sniffit is able
to give you very detailed technical info on these packets (SEQ, ACK,
TTL, Window, ...) but also packet contence in different formats (hex
or plain text, ...).

%description -l es
Sniffit is a robust non-commercial network protocol analyzer or packet
sniffer. A packet sniffer basically listens to network traffic and
produces analysis based on the traffic and/or translates packets into
some level of human readable form.

%description -l pl
Sniffit jest programem do pods³uchu pakietów TCP/UDP/ICMP. Sniffit
jest w stanie podaæ Ci bardzo wiele informacji o tych pakietach (SEQ,
ACK, TTL, Okno, ...) a tak¿e ich zawarto¶æ w ró¿nych formatach
(szesnastkowo lub w czystej postaci, ...).

%description -l pt_BR
Sniffit é um analisador de redes. Ele monitora o tráfego de rede e
produz uma análise compreensível por humanos.

%prep
%setup -q -n %{name}.%{version}.beta
%patch0 -p1
%patch1 -p1

%build
(cd libpcap
%{__aclocal}
%{__autoconf}
)
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{5,8}}

install sniffit $RPM_BUILD_ROOT%{_bindir}

install sniffit.5 $RPM_BUILD_ROOT%{_mandir}/man5
install sniffit.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PLUGIN-HOWTO README.FIRST BETA-TESTING
%doc HISTORY sample_config_file sniffit-FAQ
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
