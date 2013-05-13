Summary:	A color VT102 terminal emulator for the X Window System
Name:		rxvt-unicode
Version:	9.15
Release: 	2
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

%description
Rxvt-unicode is a clone of the well known terminal emulator rxvt, modified to
store text in Unicode (either UCS-2 or UCS-4) and to use locale-correct input
and output. It also supports mixing multiple fonts at the same time, including
Xft fonts.

%prep
%setup -q

%build
./autogen.sh

%configure2_5x \
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

%files
%{_bindir}/urxvt*
%{_libdir}/urxvt
%{_datadir}/applications/*.desktop
%{_mandir}/man*/*


%changelog
* Sun Jan 22 2012 Alexander Khrukin <akhrukin@mandriva.org> 9.15-1mdv2011.0
+ Revision: 764854
- version update 9.15

* Sat May 07 2011 Funda Wang <fwang@mandriva.org> 9.11-1
+ Revision: 672220
- new version 9.11

* Sun Dec 19 2010 Rémy Clouard <shikamaru@mandriva.org> 9.10-1mdv2011.0
+ Revision: 623036
- bump release

* Tue Nov 30 2010 Rémy Clouard <shikamaru@mandriva.org> 9.09-1mdv2011.0
+ Revision: 603984
- Update to new release 9.09
- drop patch, 256 color mode is now provided by the --enable-256-color
  configure switch
- TODO: add terminfo file to ncurses

* Sun Sep 12 2010 Rémy Clouard <shikamaru@mandriva.org> 9.07-6mdv2011.0
+ Revision: 577760
- rebuild for new perl

* Mon Aug 09 2010 Rémy Clouard <shikamaru@mandriva.org> 9.07-5mdv2011.0
+ Revision: 568247
- rebuild for new perl 5.12.1

* Sun May 02 2010 Funda Wang <fwang@mandriva.org> 9.07-4mdv2010.1
+ Revision: 541544
- fix attr of desktop file

* Sun Mar 28 2010 Rémy Clouard <shikamaru@mandriva.org> 9.07-3mdv2010.1
+ Revision: 528562
- rel++
- apply 256 color patch

* Wed Dec 30 2009 Frederik Himpe <fhimpe@mandriva.org> 9.07-1mdv2010.1
+ Revision: 483946
- Update to new version 9.07
- Remove build fix integrated upstream

* Fri Oct 09 2009 Olivier Blin <blino@mandriva.org> 9.06-4mdv2010.0
+ Revision: 456354
- buildrequire libx11-common to fix build with xim (#47140)

* Fri Sep 18 2009 Pascal Terjan <pterjan@mandriva.org> 9.06-3mdv2010.0
+ Revision: 444390
- constness fixes (partially from shikamaru)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Nov 09 2008 Funda Wang <fwang@mandriva.org> 9.06-1mdv2009.1
+ Revision: 301307
- New version 9.06

* Mon Jun 16 2008 Funda Wang <fwang@mandriva.org> 9.05-1mdv2009.0
+ Revision: 219365
- New version 9.05

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat Feb 02 2008 Funda Wang <fwang@mandriva.org> 9.02-1mdv2008.1
+ Revision: 161425
- update to new version 9.02

* Thu Jan 31 2008 Bogdano Arendartchuk <bogdano@mandriva.com> 9.01-2mdv2008.1
+ Revision: 160787
- enable xim in order to use composed accent marks

* Sat Jan 26 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 9.01-1mdv2008.1
+ Revision: 158453
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 24 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 8.9-1mdv2008.1
+ Revision: 137595
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 16 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 8.8-1mdv2008.1
+ Revision: 120493
- new version

* Sun Nov 25 2007 Funda Wang <fwang@mandriva.org> 8.7-1mdv2008.1
+ Revision: 111883
- update to new version 8.7

* Thu Nov 22 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 8.5a-1mdv2008.1
+ Revision: 111079
- new version
- new version

* Wed Nov 07 2007 Funda Wang <fwang@mandriva.org> 8.4-2mdv2008.1
+ Revision: 106709
- rebuild for new lzma

* Sun Oct 28 2007 Funda Wang <fwang@mandriva.org> 8.4-1mdv2008.1
+ Revision: 102837
- fix desktop entry

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - new version
    - remove buildrequires on desktop-file-utils - desktop file doesn't belong to the upstream tarball

* Thu Aug 02 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 8.3-1mdv2008.0
+ Revision: 57913
- new version
- tune up desktop file

* Wed Jun 13 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 8.2-1mdv2008.0
+ Revision: 38672
- make it work
- add xdg menu entry
- new version

