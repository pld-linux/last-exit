Summary:	GTK+ Last.fm player
Summary(pl):	Odtwarzacz Last.fm dla GTK+
Name:		last-exit
Version:	1.0
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://www.o-hand.com/~iain/last-exit/%{name}-%{version}.tar.bz2
# Source0-md5:	ed579d0358624ebee677d24f25be0273
Patch0:		%{name}-exec.patch
URL:		http://www.o-hand.com/~iain/last-exit/
BuildRequires:	dotnet-gtk-sharp2-gnome-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	mono-csharp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Last Exit is a player for Last.fm.

%description -l pl
Last Exit to odtwarzacz Last.fm.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install last-exit.schemas
%gconf_schema_install lastfm.schemas

%preun
%gconf_schema_uninstall last-exit.schemas
%gconf_schema_uninstall lastfm.schemas

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.exe*
%attr(755,root,root) %{_libdir}/%{name}/*.so*
%{_libdir}/%{name}/*.la
%{_sysconfdir}/gconf/schemas/*
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/apps/last-exit*
