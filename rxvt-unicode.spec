Summary:	A color VT102 terminal emulator for the X Window System
Name:		rxvt-unicode
Version:	9.22
Release: 	1
License:	GPLv2+
Group:		Terminals
URL:		http://dist.schmorp.de/rxvt-unicode
Source:		http://dist.schmorp.de/rxvt-unicode/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
# X11 locales are required to build IM support
BuildRequires:	libx11-common
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xft)
BuildRequires:	libstdc++-static-devel
BuildRequires:	pkgconfig(xrender)
BuildRequires:	fontconfig-devel

Provides:	urxvt = %{EVRD}

%description
Rxvt-unicode is a clone of the well known terminal emulator rxvt, modified to
store text in Unicode (either UCS-2 or UCS-4) and to use locale-correct input
and output. It also supports mixing multiple fonts at the same time, including
Xft fonts.

%prep
%setup -q
find . -type f -exec chmod a+r {} \;
sed -i 's,#! perl,#!%{_bindir}/perl,g' src/perl/*

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
	--enable-256-color

%make

%install
%makeinstall_std

install -D -m644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%name.desktop
chmod +x %{buildroot}/%{_libdir}/urxvt/perl/*
%files
%{_bindir}/urxvt*
%{_libdir}/urxvt
%{_datadir}/applications/*.desktop
%{_mandir}/man*/*
