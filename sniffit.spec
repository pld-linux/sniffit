Summary:	Program for demonstrating the unsafeness of TCP
Summary(pl):	Program do nas³uchu po³±czeñ TCP/UDP/ICMP
Name:		sniffit
Version:	0.3.7
Release:	2
Copyright:	Free
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Url:		http://reptile.rug.ac.be/~coder/sniffit/sniffit.html
Source:		%{name}.%{version}.beta.tar.gz 
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

%build
CFLAGS=$RPM_OPT_FLAGS LDFLAGS=-s \
./configure --prefix=%{_prefix}

make OBJ_FLAG="-w $RPM_OPT_FLAGS -c"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -s sniffit $RPM_BUILD_ROOT%{_bindir}

gzip -9nf 	PLUGIN-HOWTO README.FIRST BETA-TESTING \
		HISTORY sample_config_file sniffit-FAQ

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) %{_bindir}/*
