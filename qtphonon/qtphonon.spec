Name:       qt5-phonon
Summary:    Qt phonon module
Version:    4.9.90.20110701+gc584633
Release:    1%{?dist}
Group:      System/Libraries
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}.tar.gz
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtxml-devel
BuildRequires:  qt5-qtdbus-devel
BuildRequires:  qt5-qtopengl-devel
BuildRequires:  qt5-qmake
BuildRequires:  gstreamer-devel
BuildRequires:  gst-plugins-base-devel
BuildRequires:  fdupes

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt phonon module


%package devel
Summary:    Qt phonon - development files
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt phonon module development files

%package plugin-gstreamer
Summary:    Qt phonon GStreamer plugin
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description plugin-gstreamer
This package contains the GStreamer plugin for phonon



#### Build section

%prep
%setup -q -n %{name}


%build
export QTDIR=/usr/share/qt5
qmake
make %{?_smp_flags}

%install
rm -rf %{buildroot}
%make_install
%fdupes %{buildroot}/%{_includedir}




#### Pre/Post section

%post
/sbin/ldconfig
%postun
/sbin/ldconfig




#### File section


%files
%defattr(-,root,root,-)
%{_libdir}/libphonon.so.5
%{_libdir}/libphonon.so.5.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libphonon.so
%{_libdir}/pkgconfig/*
%{_includedir}/qt5/phonon/

%files plugin-gstreamer
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/phonon_backend/libphonon_gstreamer.so



#### Changelog section

%changelog
* Mon Jul 11 2011 Mika Boström <mika.bostrom@nomovok.com> - 4.9.90.20110701
- Initial packaging
- Builds against packages from qtbase build
