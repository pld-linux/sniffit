Summary:	Program for demonstrating the unsafeness of TCP
Summary(pl):	Program do nas�uchu po��cze� TCP/UDP/ICMP
Name:		sniffit
Version:	0.3.7
Release:	2
Copyright:	Free
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narz�dzia
Url:		http://reptile.rug.ac.be/~coder/sniffit/sniffit.html
Source:		%{name}.%{version}.beta.tar.gz 
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Sniffit is a packet sniffer for TCP/UDP/ICMP packets. Sniffit is able to
give you very detailed technical info on these packets (SEQ, ACK, TTL,
Window, ...) but also packet contence in different formats (hex or plain
text, ...).

%description -l pl
Sniffit jest programem do pods�uchu pakiet�w TCP/UDP/ICMP. Sniffit jest w stanie
poda� Ci bardzo wiele informacji o tych pakietach (SEQ, ACK, TTL, Okno, ...)
a tak�e ich zawarto�� w r�nych formatach (szesnastkowo lub w czystej postaci,
...).

%prep
%setup -q -n %{name}.%{version}.beta

%build
CFLAGS=$RPM_OPT_FLAGS LDFLAGS=-s \
./configure --prefix=%{_prefix}

make OBJ_FLAG="-w $RPM_OPT_FLAGS -c"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -s sniffit $RPM_BUILD_ROOT%{_bindir}

gzip -9fn	PLUGIN-HOWTO README.FIRST BETA-TESTING \
		HISTORY sample_config_file sniffit-FAQ

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) %{_bindir}/*

%changelog
* Thu Jul 22 1999 Wojtek �lusarczyk <wojtek@shadow.eu.org>
- build for 1.3 PLD Linux 

* Wed Oct 21 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [0.3.7-1d]
- build against 1.1 PLD,
- translation modified for pl,
- build from non root's account,
- major changes (follow the Linux PLD policy).

* Wed Jul 22 1998 Arkadiusz Mi�kiewicz <misiek@misiek.eu.org>
- updated to 0.3.7.beta
- removed old patch
