%define _qtmodule_snapshot_version %nil
Name:       qt5-qtquick1
Summary:    Qt Quick 1
Version:    %{_qtmodule_snapshot_version}
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qtopengl-devel
BuildRequires:  qt5-qtqml-devel
BuildRequires:  qt5-qtqml-qtquick-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  fdupes

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt Quick 1 library


%package devel
Summary:        Qt Quick 1 - development files
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt Quick 1 development files


%package qmlviewer
Summary:        Qt Quick 1 - standalone viewer
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description qmlviewer
Qmlviewer allows to view, or "play" Qt Quick 1 files.


%package import-folderlistmodel
Summary:        Qt Quick 1 - folderlistmodel import
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description import-folderlistmodel
This package provides Qt Quick 1 folderlistmodel import.

%package import-gestures
Summary:        Qt Quick 1 - gestures import
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description import-gestures
This package provides Qt Quick 1 gestures import.

%package import-particles
Summary:        Qt Quick 1 - particles import
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description import-particles
This package provides Qt Quick 1 particles import.

%package import-shaders
Summary:        Qt Quick 1 - shaders import
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description import-shaders
This package provides Qt Quick 1 shaders import.

%package plugin-qmltooling
Summary:        Qt Quick 1 - qmltooling plugin
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description plugin-qmltooling
This package provides Qt Quick 1 tooling plugin.

#### Build section

%prep
%setup -q -n %{name}

%build
export QTDIR=/usr/share/qt5
%qmake CONFIG+=package
make %{?_smp_flags}

%install
rm -rf %{buildroot}
%qmake_install
# Fix wrong path in pkgconfig files
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
-exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;
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
%{_libdir}/libQtQuick1.so.5
%{_libdir}/libQtQuick1.so.5.*


%files devel
%defattr(-,root,root,-)
%{_libdir}/libQtQuick1.so
%{_libdir}/libQtQuick1.prl
%{_includedir}/qt5/QtQuick1/
%{_includedir}/qt5/Qt/QtQuick1
%{_includedir}/qt5/Qt/qdeclarative*
%{_includedir}/qt5/Qt/qtquick1*
%{_libdir}/pkgconfig/QtQuick1.pc
%{_libdir}/cmake/Qt5Quick1/
%{_datadir}/qt5/mkspecs/modules/qt_quick1.pri

%files qmlviewer
%defattr(-,root,root,-)
%{_bindir}/qmlviewer

%files import-folderlistmodel
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/QtQuick1/Qt/labs/folderlistmodel/

%files import-gestures
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/QtQuick1/Qt/labs/gestures/

%files import-particles
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/QtQuick1/Qt/labs/particles/

%files import-shaders
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/QtQuick1/Qt/labs/shaders/

%files plugin-qmltooling
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/qmltooling/


#### No changelog section, separate $pkg.changes contains the history

