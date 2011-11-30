%define _qtmodule_snapshot_version %nil
Name:       qt5-qtphonon
Summary:    Qt phonon module
Version:    %{_qtmodule_snapshot_version}
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.gz
Patch0:     create_prl_and_pc_files.patch
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtxml-devel
BuildRequires:  qt5-qtdbus-devel
BuildRequires:  qt5-qtopengl-devel
BuildRequires:  qt5-qtwidgets-devel
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
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt phonon module development files

%package plugin-gstreamer
Summary:    Qt phonon GStreamer plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-gstreamer
This package contains the GStreamer plugin for phonon



#### Build section

%prep
%setup -q -n %{name}
%patch0 -p1


%build
export QTDIR=/usr/share/qt5
qmake
make %{?_smp_flags}

%install
rm -rf %{buildroot}
%qmake_install
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/"{} \;
# Remove unneeded .la files
rm -f %{buildroot}/%{_libdir}/*.la
#
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
%{_libdir}/libphonon.prl
%{_libdir}/pkgconfig/*
%{_includedir}/qt5/phonon/
%{_libdir}/cmake/

%files plugin-gstreamer
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/phonon_backend/libphonon_gstreamer.so



#### No changelog section, separate $pkg.changes contains the history
