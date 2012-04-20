%define _qtmodule_snapshot_version %nil
Name:       qt5-qtlocation
Summary:    Qt Location module
Version:    %{_qtmodule_snapshot_version}
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.gz
Patch0:     disable_demos_and_examples.patch
Patch1:     create_prl_and_pc_files.patch
Patch2:     mapsgl-define-gl-depth.patch
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qtopengl-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qtqml-devel
BuildRequires:  qt5-qtqml-qtquick-devel
BuildRequires:  qt5-qt3d-devel
BuildRequires:  qt5-qmake
BuildRequires:  fdupes

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt location module


%package devel
Summary:    Qt location - development files
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt location module development files


%package -n qt5-qtqml-import-location
Summary:    QtQml location import
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}
Requires:   qt5-qtqml

%description -n qt5-qtqml-import-location
This package contains the Location import for QtQml

%package plugin-geoservices-nokia
Summary:    Qt Geoservices plugin for Nokia devices
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-geoservices-nokia
This package contains the geoservices plugin for Nokia devices

#### Build section

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
#%patch2 -p1


%build
export QTDIR=/usr/share/qt5
qmake
make %{?_smp_flags}

%install
rm -rf %{buildroot}
%qmake_install
# Remove unneeded .la files
rm -f %{buildroot}/%{_libdir}/*.la
# Fix wrong path in pkgconfig files
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
-exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;
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
%{_libdir}/libQtLocation.so.5
%{_libdir}/libQtLocation.so.5.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libQtLocation.so
%{_libdir}/libQtLocation.prl
%{_libdir}/pkgconfig/*
%{_includedir}/qt5/*
%{_datadir}/qt5/mkspecs/
%{_libdir}/cmake/Qt5Location/

%files -n qt5-qtqml-import-location
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/QtLocation/

%files plugin-geoservices-nokia
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/geoservices/


#### No changelog section, separate $pkg.changelog contains the history
