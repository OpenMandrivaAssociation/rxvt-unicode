Summary:	A color VT102 terminal emulator for the X Window System
Name:		rxvt-unicode
Version:	7.6
Release: 	%mkrel 2
License:	GPL
Group:		Terminals
URL:		http://dist.schmorp.de/rxvt-unicode/
Source:		http://sourceforge.net/projects/rxvt-unicode/%name-%{version}.tar.bz2

Buildroot:	%{_tmppath}/%name-%{version}-%{release}-root
BuildRequires:	XFree86-devel xpm-devel utempter-devel perl-base


%description
Rxvt-unicode is a clone of the well known terminal emulator rxvt, modified to
store text in Unicode (either UCS-2 or UCS-4) and to use locale-correct input
and output. It also supports mixing multiple fonts at the same time, including
Xft fonts.

%prep
%setup -q

%build

export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -DUTEMPTER"  
%configure --prefix=/usr/X11R6 --enable-everything --with-terminfo --libdir=%_libdir \
	--enable-xpm-background --enable-menubar \
	--enable-utmp --enable-ttygid \
	--enable-transparency --enable-next-scroll --enable-rxvt-scroll --enable-xterm-scroll \
	--enable-xim --enable-languages --enable-smart-resize  \
	--enable-mousewheel --enable-static=yes

%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

mkdir -p $RPM_BUILD_ROOT%_prefix/X11R6/bin
mkdir -p $RPM_BUILD_ROOT%_prefix/X11R6/man/man1
mkdir -p $RPM_BUILD_ROOT%_prefix/X11R6/man/man7
mv $RPM_BUILD_ROOT%_bindir/* $RPM_BUILD_ROOT%_prefix/X11R6/bin/
mv $RPM_BUILD_ROOT%_mandir/man1/* $RPM_BUILD_ROOT%_prefix/X11R6/man/man1/
mv $RPM_BUILD_ROOT%_mandir/man7/* $RPM_BUILD_ROOT%_prefix/X11R6/man/man7/

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%name
?package(%name):\
 needs=x11 section="Terminals" title="Rxvt-unicode"\
  longtitle="Rxvt clone terminal with support for Unicode"\
  command="/usr/X11R6/bin/urxvt" icon="terminals_section.png"
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/*
/usr/X11R6/man/man1/*
/usr/X11R6/man/man7/*
%_libdir/urxvt
#%config(missingok,noreplace) /etc/rxvt/rxvt-zh.menu
%{_menudir}/%name
%_mandir/man3/*

