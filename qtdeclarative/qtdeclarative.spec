%define _qtmodule_snapshot_version %nil
%define _qtmodule_name qt5-qtdeclarative
 
Name:       qt5-qtqml
Summary:    Qt Declarative library
Version:    %{_qtmodule_snapshot_version}
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{_qtmodule_name}-%{version}.tar.gz
Patch0:     create_prl_and_pc_files.patch
Patch1:     fix-destdir.patch
Patch10:    particles-shader-fix.patch
Patch11:    glsl-highp-ambiguity.patch
Patch50:    0001-Fix-modular-build.patch
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

#%package import-inputcontext
#Summary:    Qt Declarative input context plugin
#Group:      Qt/Qt
#Requires:   %{name} = %{version}-%{release}
#
#%description import-inputcontext
#This package provides the QtDeclarative input context plugin

#%package import-particles
#Summary:    Qt Declarative particles plugin
#Group:      Qt/Qt
#Requires:   %{name} = %{version}-%{release}
#
#%description import-particles
#This package provides the QtDeclarative particles plugin

%package plugin-qmlinspector
Summary:    Qt Declarative QML inspector plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-qmlinspector
This package provides the QML inspector plugin

%package plugin-accessible
Summary:    Qt Declarative accessible plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-accessible
This package provides the QML accessible plugin


%package import-qt47plugin
Summary:    Qt Declarative Qt 4.7 legacy support plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description import-qt47plugin
This package provides the legacy Qt 4.7 support plugin

%package import-qtquick2plugin
Summary:    Qt Declarative QtQuick 2 support plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description import-qtquick2plugin
This package provides the QtQuick 2 support plugin

%package import-qttest
Summary:    Qt Declarative QtTest plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description import-qttest
This package provides the QtQml QtTest plugin

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
%patch0 -p1
%patch10 -p1
%patch11 -p1
#%patch50 -p1


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
# Manually copy qmldevtools static library
cp lib/libQtQmlDevTools.a %{buildroot}/%{_libdir}
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

%post qtquick
/sbin/ldconfig
%postun qtquick
/sbin/ldconfig





#### File section


%files
%defattr(-,root,root,-)
%{_libdir}/libQtQml.so.5
%{_libdir}/libQtQml.so.5.*

# FIXME: the provided .pc file is empty!
# Find out what gives and find a clean resolution
%files devel
%defattr(-,root,root,-)
%{_libdir}/libQtQml.so
%{_libdir}/libQtQml.prl
%{_libdir}/pkgconfig/QtQml.pc
%{_includedir}/qt5/Qt/qqml*.h
%{_includedir}/qt5/Qt/qtqml*.h
%{_includedir}/qt5/Qt/qsg*.h
%{_includedir}/qt5/Qt/qjs*.h
%{_includedir}/qt5/Qt/QJS*
%{_includedir}/qt5/Qt/QDeclarative*
%{_includedir}/qt5/Qt/designersupport.h
%{_includedir}/qt5/Qt/QtQml
%{_includedir}/qt5/QtQml/
%{_includedir}/qt5/QtDeclarative/
%{_includedir}/qt5/Qt/QtDeclarative
%{_includedir}/qt5/Qt/QDeclarative*
%{_includedir}/qt5/Qt/QJS*
%{_includedir}/qt5/Qt/qdecl*.h
%{_includedir}/qt5/Qt/qtdeclarativeversion.h
%{_datadir}/qt5/mkspecs/modules/qt_declarative.pri
%{_datadir}/qt5/mkspecs/modules/qt_qml.pri
%{_libdir}/cmake/


%files qtquick
%defattr(-,root,root,-)
%{_libdir}/libQtQuick.so.5
%{_libdir}/libQtQuick.so.5.*

%files qtquick-devel
%defattr(-,root,root,-)
%{_libdir}/libQtQuick.so
%{_libdir}/libQtQuick.prl
%{_libdir}/pkgconfig/QtQuick.pc
%{_includedir}/qt5/Qt/qtquickversion.h
%{_includedir}/qt5/Qt/qtquickglobal.h
%{_includedir}/qt5/Qt/qquick*.h
%{_includedir}/qt5/Qt/QtQuick
%{_includedir}/qt5/QtQuick/
%{_datadir}/qt5/mkspecs/modules/qt_quick.pri






%files qmlscene
%defattr(-,root,root,-)
%{_bindir}/qmlscene

%files devel-tools
%defattr(-,root,root,-)
%{_bindir}/qmlplugindump
%{_bindir}/qmlprofiler
%{_bindir}/qmltestrunner
%{_bindir}/qmlmin



%files import-folderlistmodel
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/Qt/labs/folderlistmodel/*

%files import-localstorageplugin
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/QtQuick/LocalStorage/

#%files import-inputcontext
#%defattr(-,root,root,-)
#%{_libdir}/qt5/imports/Qt/labs/inputcontext/*

#%files import-particles
#%defattr(-,root,root,-)
#%{_libdir}/qt5/imports/Qt/labs/particles/*

%files plugin-qmlinspector
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/qmltooling/*

%files plugin-accessible
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/accessible/*


%files import-qttest
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/QtTest/

%files import-qt47plugin
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/Qt/

%files import-qtquick2plugin
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/QtQuick.2/





%files qtquicktest
%defattr(-,root,root,-)
%{_libdir}/libQtQuickTest.so.5
%{_libdir}/libQtQuickTest.so.5.*

%files qtquicktest-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/qtquicktest*.h
%{_includedir}/qt5/Qt/quicktest*.h
%{_includedir}/qt5/Qt/QtQuickTest
%{_includedir}/qt5/QtQuickTest/
%{_libdir}/libQtQuickTest.so
%{_libdir}/libQtQuickTest.prl
%{_libdir}/pkgconfig/QtQuickTest.pc
%{_datadir}/qt5/mkspecs/modules/qt_qmltest.pri

%files qtqmltools-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/QtQmlDevTools
%{_includedir}/qt5/QtQmlDevTools/
%{_libdir}/libQtQmlDevTools.a
%{_libdir}/libQtQmlDevTools.prl
%{_libdir}/pkgconfig/QtQmlDevTools.pc
%{_datadir}/qt5/mkspecs/modules/qt_qmldevtools.pri









#### No changelog section, separate $pkg.changelog contains the history
