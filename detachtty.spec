#
%define		_snapshot	bese20071213
Summary:	An utility that lets you run interactive programs non-interactively
Summary(pl.UTF-8):	Narzędzie pozwalające na nieinteraktywne uruchamianie interaktywnych programów
Name:		detachtty
Version:	0.%{_snapshot}
Release:	1
License:	GPL v2
Group:		Applications
#		darcs get http://common-lisp.net/project/bese/repos/detachtty/
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	9ad00851091df6ecf40489ef83c668f7
URL:		http://www.cliki.net/detachtty
Suggests:	openssh-clients
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Detachtty is a Unix utility that lets you run interactive programs
(such as Lisp) non-interactively. Also, it allows you to connect to
them over the network when you do need to interact with them. It is
intended for use with long-running server processes running in Common
Lisp implementations.

%description -l pl.UTF-8
Detachtty jest uniksowym narzędziem pozwalającym na uruchamianie
programów interaktywnych (jak Lisp) w sposób nieinteraktywny.
Ponadto, pozwala połączyć się z tymi procesami przez sieć, gdy
zachodzi potrzeba interakcji.  Stworzony został z myślą o długo
działających procesach uruchomionych w środowisku Common Lisp.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags} -DNEED_PTY_H" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_DIR=%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
