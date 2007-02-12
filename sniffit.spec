Summary:	Program for demonstrating the unsafeness of TCP
Summary(es.UTF-8):   Programa para demonstrar la inseguridad de TCP
Summary(pl.UTF-8):   Program do nasłuchu połączeń TCP/UDP/ICMP
Summary(pt_BR.UTF-8):   Um analisador de protocolos de rede
Name:		sniffit
Version:	0.3.7
Release:	9
Epoch:		1
License:	distributable
Group:		Networking/Utilities
Source0:	http://reptile.rug.ac.be/~coder/sniffit/files/%{name}.%{version}.beta.tar.gz
# Source0-md5:	2697cc18878480199fe6db1e61134d5a
Patch0:		%{name}-fixes.patch
Patch1:		%{name}-gcc33.patch
Patch2:		%{name}-am18.patch
URL:		http://reptile.rug.ac.be/~coder/sniffit/sniffit.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sniffit is a packet sniffer for TCP/UDP/ICMP packets. Sniffit is able
to give you very detailed technical info on these packets (SEQ, ACK,
TTL, Window, ...) but also packet contents in different formats (hex
or plain text, ...).

%description -l es.UTF-8
Sniffit es un sniffer de paquetes TCP/UDP/ICMP. Es capaz de dar
información técnica muy detallada sobre esos paquetes (SEQ, ACK, TTL,
ventana, ...), igual que su contenido en varios formatos (hex, texto
plano, ...).

%description -l pl.UTF-8
Sniffit jest programem do podsłuchu pakietów TCP/UDP/ICMP. Sniffit
jest w stanie podać Ci bardzo wiele informacji o tych pakietach (SEQ,
ACK, TTL, Okno, ...) a także ich zawartość w różnych formatach
(szesnastkowo lub w czystej postaci, ...).

%description -l pt_BR.UTF-8
Sniffit é um analisador de redes. Ele monitora o tráfego de rede e
produz uma análise compreensível por humanos.

%prep
%setup -q -n %{name}.%{version}.beta
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cd libpcap
cp -f /usr/share/automake/config.sub .
mv -f aclocal.m4 acinclude.m4
%{__aclocal}
%{__autoconf}
cd ..

cp -f /usr/share/automake/config.sub .
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
