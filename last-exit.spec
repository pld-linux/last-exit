#
%include	/usr/lib/rpm/macros.mono
#
Summary:	GTK+ Last.fm player
Summary(pl.UTF-8):	Odtwarzacz Last.fm dla GTK+
Name:		last-exit
Version:	6
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://lastexit-player.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	ef0bffe352073b7663441aa9b80237b1
Patch0:		%{name}-exec.patch
Patch1:		%{name}-desktop.patch
URL:		http://lastexit-player.org/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	dotnet-gnome-sharp-devel >= 2.15.0
BuildRequires:	dotnet-ndesk-dbus-glib-sharp-devel >= 0.4.1
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.9
BuildRequires:	libsexy-devel >= 0.1.5
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	rpmbuild(macros) >= 1.176
Requires(post,postun):	gtk+2 >= 2.10.2
Requires(post,preun):	GConf2 >= 2.14.0
Requires:	dotnet-gnome-sharp >= 2.16.0
Requires:	dotnet-gtk-sharp2 >= 2.10.0
Requires:	gstreamer-audio-effects-base >= 0.10.9
Requires:	gstreamer-audio-formats >= 0.10.4
Requires:	gstreamer-audiosink
Requires:	mono
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Last Exit is a player for Last.fm.

%description -l pl.UTF-8
Last Exit to odtwarzacz Last.fm.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install last-exit.schemas
%gconf_schema_install lastfm.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall last-exit.schemas
%gconf_schema_uninstall lastfm.schemas

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.exe*
%attr(755,root,root) %{_libdir}/%{name}/*.so
%attr(755,root,root) %{_libdir}/%{name}/*.dll
%{_sysconfdir}/gconf/schemas/last-exit.schemas
%{_sysconfdir}/gconf/schemas/lastfm.schemas
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/apps/last-exit*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/icons
