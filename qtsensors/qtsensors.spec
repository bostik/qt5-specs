%define _qtmodule_snapshot_version %nil
Name:       qt5-qtsensors
Summary:    Qt Sensors module
Version:    %{_qtmodule_snapshot_version}
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtopengl-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qtqml-devel
BuildRequires:  qt5-qmake
BuildRequires:  fdupes
BuildRequires:  gdb

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt sensors module


%package devel
Summary:    Qt sensors - development files
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt sensors module development files


%package plugin-dummy
Summary:    Dummy sensors plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-dummy
This package contains the dummy plugin for sensors

%package plugin-generic
Summary:    Generic sensors plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-generic
This package contains the generic plugin for sensors

%package plugin-linuxsys
Summary:    Linux system sensors plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-linuxsys
This package contains the linux system plugin for sensors

%package plugin-gestures-shake
Summary:    Shake gesture plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-gestures-shake
This package contains the shake gesture plugin for sensors

%package plugin-gestures-sensor
Summary:    Sensor gesture plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-gestures-sensor
This package contains the gesture plugin for sensors

#### Build section

%prep
%setup -q -n %{name}


%build
export QTDIR=/usr/share/qt5
qmake
make %{?_smp_flags}

%install
rm -rf %{buildroot}
%qmake_install
# Remove unneeded .la files
rm -f %{buildroot}/%{_libdir}/*.la
%fdupes %{buildroot}/%{_includedir}




#### Pre/Post section

%post
/sbin/ldconfig
%postun
/sbin/ldconfig




#### File section


%files
%defattr(-,root,root,-)
%{_libdir}/libQt5Sensors.so.5
%{_libdir}/libQt5Sensors.so.5.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libQt5Sensors.so
%{_libdir}/libQt5Sensors.prl
%{_libdir}/pkgconfig/*
%{_includedir}/qt5/*
%{_datadir}/qt5/mkspecs/
%{_libdir}/cmake/


%files plugin-dummy
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/sensors/libqtsensors_dummy.so

%files plugin-generic
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/sensors/libqtsensors_generic.so

%files plugin-linuxsys
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/sensors/libqtsensors_linuxsys.so

%files plugin-gestures-shake
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/sensorgestures/libqtsensorgestures_shakeplugin.so

%files plugin-gestures-sensor
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/sensorgestures/libqtsensorgestures_plugin.so


#### No changelog section, separate $pkg.changes contains the history
