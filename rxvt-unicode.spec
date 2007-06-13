Summary:	A color VT102 terminal emulator for the X Window System
Name:		rxvt-unicode
Version:	8.2
Release: 	%mkrel 1
License:	GPL
Group:		Terminals
URL:		http://dist.schmorp.de/rxvt-unicode
Source:		http://dist.schmorp.de/rxvt-unicode/%{name}-%{version}.tar.bz2
BuildRequires:	X11-devel
BuildRequires:	fontconfig-devel
BuildRequires:	glib2-devel
BuildRequires:	utempter-devel
BuildRequires:	perl-devel
BuildRequires:	oxim
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Rxvt-unicode is a clone of the well known terminal emulator rxvt, modified to
store text in Unicode (either UCS-2 or UCS-4) and to use locale-correct input
and output. It also supports mixing multiple fonts at the same time, including
Xft fonts.

%prep
%setup -q

%build
./autogen.sh
#xport CFLAGS="%{optflags} -D_GNU_SOURCE -DUTEMPTER"
%configure2_5x \
	--enable-everything
#--prefix=%{_prefix} \
#--enable-everything \
#--with-terminfo \
#--libdir=%{_libdir} \
#--enable-xpm-background \
#--enable-menubar \
#--enable-utmp \
#--enable-ttygid \
#--enable-transparency \
#--enable-next-scroll \
#--enable-rxvt-scroll \
#--enable-xterm-scroll \
#--enable-xim \
#--enable-languages \
#--enable-smart-resize \
#--enable-mousewheel \
#--enable-static=yes

%make

%install
rm -rf %{buildroot}
%makeinstall_std

#kdir -p $RPM_BUILD_ROOT%_prefix/X11R6/bin
#kdir -p $RPM_BUILD_ROOT%_prefix/X11R6/man/man1
#kdir -p $RPM_BUILD_ROOT%_prefix/X11R6/man/man7
#v $RPM_BUILD_ROOT%_bindir/* $RPM_BUILD_ROOT%_prefix/X11R6/bin/
#v $RPM_BUILD_ROOT%_mandir/man1/* $RPM_BUILD_ROOT%_prefix/X11R6/man/man1/
#v $RPM_BUILD_ROOT%_mandir/man7/* $RPM_BUILD_ROOT%_prefix/X11R6/man/man7/

#kdir -p $RPM_BUILD_ROOT%{_menudir}
#at << EOF > $RPM_BUILD_ROOT%{_menudir}/%name
#package(%name):\
#needs=x11 section="Terminals" title="Rxvt-unicode"\
# longtitle="Rxvt clone terminal with support for Unicode"\
# command="/usr/X11R6/bin/urxvt" icon="terminals_section.png"
#OF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
#usr/X11R6/bin/*
#usr/X11R6/man/man1/*
#usr/X11R6/man/man7/*
#_libdir/urxvt
#%config(missingok,noreplace) /etc/rxvt/rxvt-zh.menu
#{_menudir}/%name
#_mandir/man3/*

