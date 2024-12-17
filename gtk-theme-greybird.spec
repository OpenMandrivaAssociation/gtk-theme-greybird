%define _buildnumber c7987a8
%define _revision 7
%define oname Greybird

Summary:	A Clean Minimalistic Theme for GNOME, XFCE, GTK+ 2 and 3
Name:		gtk-theme-greybird
Version:	3.23.4
Release:	1
Group:		Graphical desktop/GNOME
License:	GPL-2.0+ or CC-BY-SA-3.0
URL:		http://shimmerproject.org/project/greybird/
Source0:	https://github.com/shimmerproject/Greybird/archive/refs/tags/v%{version}/Greybird-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:  meson
BuildRequires:  sassc
BuildRequires:  glib2.0-common
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  librsvg2

%description
This theme for GTK2/3 and xfwm4/emerald/metacity started out on the basis of
Bluebird, but aims at reworking the intense blue tone to a more neutral
grey-ish look that will be more pleasant to look at in everyday use.

%package common
Summary:	A Clean Minimalistic Theme for GNOME, XFCE, GTK+ 2 and 3 -- Common Files

%description common
The Greybird theme for GTK2/3 and xfwm4/emerald/metacity started out on the
basis of Bluebird, but aims at reworking the intense blue tone to a more
neutral grey-ish look that will be more pleasant to look at in everyday use.

This package provides the files common to the GTK+ themes and the window
manager themes as well as background images.

%package -n gtk2-theme-greybird
Summary:	A Clean Minimalistic Theme for GNOME, XFCE, GTK+ 2 and 3 -- GTK+ 2 Support
Requires:	%{name}-common = %{version}
Requires:	murrine

%description -n gtk2-theme-greybird
This package provides the GTK+ 2 support of Greybird.

%package -n gtk3-theme-greybird
Summary:	A Clean Minimalistic Theme for GNOME, XFCE, GTK+ 2 and 3 -- GTK+ 3 Support
Requires:	%{name}-common = %{version}
Requires:	gtk-unico-engine

%description -n gtk3-theme-greybird
This package provides the GTK+ 3 support of Greybird.

%prep
%autosetup -n %{oname}-%{version} -p1

%build
%meson
%meson_install

%install
%meson_build

%files common
%doc README LICENSE.CC LICENSE.GPL
%dir %{_datadir}/themes/%{_name}/
%{_datadir}/themes/%{_name}/backdrops
%{_datadir}/themes/%{_name}/metacity-1
%{_datadir}/themes/%{_name}/xfce-notify-4.0
%{_datadir}/themes/%{_name}/xfwm4
%{_datadir}/themes/%{_name}/xfwm4_compact
%{_datadir}/themes/%{_name}/Greybird.emerald

%files -n gtk2-theme-greybird
%{_datadir}/themes/%{_name}/gtk-2.0

%files -n gtk3-theme-greybird
%{_datadir}/themes/%{_name}/gtk-3.0



%changelog
* Fri Mar 02 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.4-2
+ Revision: 781867
- rebuild, fixed requires for unico-engine name

* Fri Mar 02 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.4-1
+ Revision: 781824
- new version v0.4-7-gc7987a8
- cleaned up spec
- renamed pkg to mdv std
- imported package greybird-theme

