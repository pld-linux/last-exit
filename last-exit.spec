Summary:	GTK+ Last.fm player
Summary(pl):	Odtwarzacz Last.fm dla GTK+
Name:		last-exit
Version:	2.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://www.o-hand.com/~iain/last-exit/%{name}-%{version}.tar.bz2
# Source0-md5:	85e31cbf8827284422d9328a71d777f2
Patch0:		%{name}-exec.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.o-hand.com/~iain/last-exit/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	dotnet-gnome-sharp-devel >= 2.15.0
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.9
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:  rpmbuild(macros) >= 1.176
Requires(post,preun):   GConf2 >= 2.14.0
Requires(post,postun):  gtk+2 >= 2.10.2
Requires:       gstreamer-audio-effects-base >= 0.10.9
Requires:       gstreamer-audio-formats >= 0.10.4
Requires:       gstreamer-audiosink
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Last Exit is a player for Last.fm.

%description -l pl
Last Exit to odtwarzacz Last.fm.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

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

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.exe*
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_sysconfdir}/gconf/schemas/last-exit.schemas
%{_sysconfdir}/gconf/schemas/lastfm.schemas
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/apps/last-exit*
