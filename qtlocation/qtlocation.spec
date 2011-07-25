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
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtopengl-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtdeclarative-qtquick1-devel
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


%package -n qt5-qtdeclarative-import-location
Summary:    QtDeclarative location import
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}
Requires:   qt5-qtdeclarative

%description -n qt5-qtdeclarative-import-location
This package contains the Location import for QtDeclarative

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
%{_libdir}/libQtLocation.so.5
%{_libdir}/libQtLocation.so.5.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libQtLocation.so
%{_libdir}/pkgconfig/*
%{_includedir}/qt5/*
%{_datadir}/qt5/mkspecs/

%files -n qt5-qtdeclarative-import-location
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/Qt/location/

%files plugin-geoservices-nokia
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/geoservices/


#### No changelog section, separate $pkg.changelog contains the history
