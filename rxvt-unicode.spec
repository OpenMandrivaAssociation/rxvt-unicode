Summary:	A color VT102 terminal emulator for the X Window System
Name:		rxvt-unicode
Version:	9.31
Release: 	5
License:	GPLv2+
Group:		Terminals
URL:		https://dist.schmorp.de/rxvt-unicode
Source0:	https://dist.schmorp.de/rxvt-unicode/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:         rxvt-unicode-9.21-Fix-hard-coded-wrong-path-to-xsubpp.patch
Patch1:         rxvt-unicode-0001-Prefer-XDG_RUNTIME_DIR-over-the-HOME.patch
# X11 locales are required to build IM support
BuildRequires:	libx11-common
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xft)
BuildRequires:	libstdc++-static-devel
BuildRequires:	pkgconfig(libptytty)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xext)
BuildRequires:	fontconfig-devel
BuildRequires:	perl-ExtUtils-Embed
BuildRequires:  ncurses

Provides:	urxvt = %{EVRD}

%description
Rxvt-unicode is a clone of the well known terminal emulator rxvt, modified to
store text in Unicode (either UCS-2 or UCS-4) and to use locale-correct input
and output. It also supports mixing multiple fonts at the same time, including
Xft fonts.

%prep
%setup -q
%autopatch -p1
find . -type f -exec chmod a+r {} \;
sed -i 's,#! perl,#!%{_bindir}/perl,g' src/perl/*

# kill the rxvt-unicode terminfo file - #192083
#sed -i -e "/rxvt-unicode.terminfo/d" doc/Makefile.in

%build
./autogen.sh

%configure \
	--enable-unicode3 \
	--enable-combining \
	--enable-xft \
	--enable-font-styles \
	--enable-transparency \
	--enable-fading \
	--enable-rxvt-scroll \
	--disable-next-scroll \
	--disable-xterm-scroll \
	--enable-perl \
	--enable-xim \
	--enable-pixbuf \
	--enable-backspace-key \
	--enable-delete-key \
	--enable-resources \
	--disable-8bitctrls \
	--enable-swapscreen \
	--enable-iso14755 \
	--enable-frills \
	--enable-keepscrolling \
	--enable-selectionscrolling \
	--enable-mousewheel \
	--enable-slipwheeling \
	--enable-smart-resize \
	--enable-text-blink \
	--enable-pointer-blank \
	--disable-utmp \
	--disable-wtmp \
	--disable-lastlog \
	--with-terminfo=%{_datadir}/%{name} \
	--enable-256-color

%make_build

%install
%make_install

install -D -m644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%name.desktop
chmod +x %{buildroot}/%{_libdir}/urxvt/perl/*
# install terminfo for 256color
mkdir -p %{buildroot}%{_datadir}/terminfo/r/
tic -e rxvt-unicode-256color -s -o %{buildroot}%{_datadir}/terminfo/ doc/etc/rxvt-unicode.terminfo

%files
%{_bindir}/urxvt*
%{_bindir}/urclock
%{_libdir}/urxvt
%{_datadir}/applications/*.desktop
%{_mandir}/man*/*
%{_datadir}/terminfo/r/rxvt-unicode-256color
