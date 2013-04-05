%define _qtmodule_snapshot_version %nil
%define _qtmodule_name qt5-qtdeclarative

# Tell rpmbuild not to remove static libraries after running install but
# before generating the packages. We want to keep the built
# libQt5QmlDevTools.a around.
%define keepstatic 1

Name:       qt5-qtqml
Summary:    Qt Declarative library
Version:    %{_qtmodule_snapshot_version}
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{_qtmodule_name}-%{version}.tar.gz
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qtopengl-devel
BuildRequires:  qt5-qtsql-devel
BuildRequires:  qt5-qttest-devel
BuildRequires:  qt5-qtv8-devel
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qmake
BuildRequires:  fdupes
BuildRequires:  python
BuildRequires:  gdb

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Declarative library


%package devel
Summary:    Qt Declarative - development files
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}
Requires:   qt5-qtsql-devel

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Declarative library development files

%package qtquicktest
Summary:    Qt Declarative QtQuickTest library
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtquicktest
This package contains the QtQuickTest library for QtDeclarative module

%package qtquicktest-devel
Summary:    Qt Declarative QtQuickTest - development files
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-devel = %{version}-%{release}
Requires:   qt5-qtqml-qtquicktest = %{version}-%{release}

%description qtquicktest-devel
This package contains the development headers for QtQuickTest library

%package qtquickparticles
Summary:    Qt Declarative - QtQuickParticles library
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description qtquickparticles
This package contains the QtQuickParticles library for QtDeclarative
module

%package qtquickparticles-devel
Summary:    Qt Declarative - QtQuickParticles development files
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}
Requires:   qt5-qtqml-qtquickparticles = %{version}-%{release}

%description qtquickparticles-devel
This package contains the development headers for QtQuickParticles
effect library

%package qtquick
Summary:    Qt Declarative - QtQuick library
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description qtquick
This package contains the QtQuick QML support library

%package qtquick-devel
Summary:    Qt Declarative - QtQuick development files
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}
Requires:   qt5-qtqml-qtquick = %{version}-%{release}

%description qtquick-devel
This package contains the development headers for legacy QtQuick 1
QML support library


%package qtqmltools-devel
Summary:    Qt Declarative QtQmlDevTools - development files
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-devel = %{version}-%{release}
Requires:   qt5-qtqml-devel = %{version}-%{release}

%description qtqmltools-devel
This package contains the development headers for QtQmlDevTools



#### Small plugin and import packages

%package import-folderlistmodel
Summary:    Qt Declarative folderlistmodel plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description import-folderlistmodel
This package provides the QtQml folderlistmodel plugin

%package import-localstorageplugin
Summary:    Qt LocalStorage plugin
Requires:   %{name} = %{version}-%{release}

%description import-localstorageplugin
This package provided the Qt LocalStorage plugin

%package import-particles
Summary:    Qt Declarative particles plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description import-particles
This package provides the QtDeclarative particles plugin for QtQuick 2.0

%package import-models
Summary:    Qt Declarative models plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description import-models
This package provides the QtDeclarative models plugin for QtQuick 2.0

%package import-dialogs
Summary:    Qt Declarative dialogs plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description import-dialogs
This package provides the QtDeclarative dialogs plugin for QtQuick 2.0

%package import-privatewidgets
Summary:    Qt Declarative private widgets plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description import-privatewidgets
This package provides the QtDeclarative private widgets plugin for QtQuick 2.0

%package import-window
Summary:    Qt Declarative window plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description import-window
This package provides the QML window plugin for QtQuick 2.0

%package plugin-qmlinspector
Summary:    Qt Declarative QML inspector plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-qmlinspector
This package provides the QML inspector plugin

%package import-qtquick2plugin
Summary:    Qt Declarative QtQuick 2 support plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description import-qtquick2plugin
This package provides the QtQuick 2 support plugin

%package plugin-qmltest
Summary:    Qt Declarative QtTest plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-qmltest
This package provides the QtQml QtTest plugin

%package plugin-accessible
Summary:    Qt Declarative accessible plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-accessible
This package provides the QtQml accessible plugin


%package qmlscene
Summary:    QML scene viewer
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description qmlscene
This package contains the QML viewer for QtQuick 2.0 files.

%package devel-tools
Summary:    QML development tools
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description devel-tools
This package contains QML debugging and development tools






#### Build section

%prep
%setup -q -n %{_qtmodule_name}

%build
export QTDIR=/usr/share/qt5
qmake
make %{?_smp_flags}

%install
rm -rf %{buildroot}
%make_install
# Fix wrong path in pkgconfig files
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
-exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;
# Remove unneeded .la files
rm -f %{buildroot}/%{_libdir}/*.la
%fdupes %{buildroot}/%{_libdir}
%fdupes %{buildroot}/%{_includedir}




#### Pre/Post section

%post
/sbin/ldconfig
%postun
/sbin/ldconfig

%post qtquicktest
/sbin/ldconfig
%postun qtquicktest
/sbin/ldconfig

%post qtquickparticles
/sbin/ldconfig
%postun qtquickparticles
/sbin/ldconfig

%post qtquick
/sbin/ldconfig
%postun qtquick
/sbin/ldconfig





#### File section


%files
%defattr(-,root,root,-)
%{_libdir}/libQt5Qml.so.5
%{_libdir}/libQt5Qml.so.5.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libQt5Qml.so
%{_libdir}/libQt5Qml.prl
%{_libdir}/pkgconfig/Qt5Qml.pc
%{_includedir}/qt5/QtQml/
%{_datadir}/qt5/mkspecs/modules/qt_lib_qml.pri
%{_libdir}/cmake/


%files qtquick
%defattr(-,root,root,-)
%{_libdir}/libQt5Quick.so.5
%{_libdir}/libQt5Quick.so.5.*

%files qtquick-devel
%defattr(-,root,root,-)
%{_libdir}/libQt5Quick.so
%{_libdir}/libQt5Quick.prl
%{_libdir}/pkgconfig/Qt5Quick.pc
%{_includedir}/qt5/QtQuick/
%{_datadir}/qt5/mkspecs/modules/qt_lib_quick.pri






%files qmlscene
%defattr(-,root,root,-)
%{_bindir}/qmlscene

%files devel-tools
%defattr(-,root,root,-)
%{_bindir}/qmlplugindump
%{_bindir}/qmlprofiler
%{_bindir}/qmltestrunner
%{_bindir}/qmlmin
%{_bindir}/qmlbundle



%files import-folderlistmodel
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/Qt/labs/folderlistmodel/*

%files import-localstorageplugin
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtQuick/LocalStorage/

%files import-particles
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtQuick/Particles.2/

%files import-models
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtQml/Models.2/

%files import-dialogs
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtQuick/Dialogs/

%files import-privatewidgets
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtQuick/PrivateWidgets/

%files import-window
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtQuick/Window.2/

%files plugin-qmlinspector
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/qmltooling/*

%files plugin-qmltest
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtTest/

%files plugin-accessible
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/accessible/

%files import-qtquick2plugin
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtQuick.2/





%files qtquicktest
%defattr(-,root,root,-)
%{_libdir}/libQt5QuickTest.so.5
%{_libdir}/libQt5QuickTest.so.5.*

%files qtquicktest-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtQuickTest/
%{_libdir}/libQt5QuickTest.so
%{_libdir}/libQt5QuickTest.prl
%{_libdir}/pkgconfig/Qt5QuickTest.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_qmltest.pri

%files qtquickparticles
%defattr(-,root,root,-)
%{_libdir}/libQt5QuickParticles.so.5
%{_libdir}/libQt5QuickParticles.so.5.*

%files qtquickparticles-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtQuickParticles/
%{_libdir}/libQt5QuickParticles.so
%{_libdir}/libQt5QuickParticles.prl
%{_libdir}/pkgconfig/Qt5QuickParticles.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_quickparticles.pri


%files qtqmltools-devel
%defattr(-,root,root,-)
#%{_includedir}/qt5/QtQmlDevTools/
%{_libdir}/libQt5QmlDevTools.a
%{_libdir}/libQt5QmlDevTools.prl
%{_libdir}/pkgconfig/Qt5QmlDevTools.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_qmldevtools.pri




#### No changelog section, separate $pkg.changelog contains the history
