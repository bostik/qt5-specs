%define _qtmodule_snapshot_version %nil

Name:       qt5-qtdeclarative
Summary:    Qt Declarative library
Version:    %{_qtmodule_snapshot_version}
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.gz
Patch0:     create_prl_and_pc_files.patch
Patch10:    particles-shader-fix.patch
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
Requires:   qt5-qtdeclarative-qtquicktest = %{version}-%{release}

%description qtquicktest-devel
This package contains the development headers for QtQuickTest library

%package qtquick1
Summary:    Qt Declarative - legacy QtQuick1 library
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description qtquick1
This package contains the legacy QtQuick 1 (non-scenegraph)
QML support library

%package qtquick1-devel
Summary:    Qt Declarative - legazy QtQuick 1 development files
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}
Requires:   qt5-qtdeclarative-qtquick1 = %{version}-%{release}

%description qtquick1-devel
This package contains the development headers for legacy QtQuick 1
QML support library


%package qtqmltools-devel
Summary:    Qt Declarative QtQmlDevTools - development files
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-devel = %{version}-%{release}
Requires:   qt5-qtdeclarative-devel = %{version}-%{release}

%description qtqmltools-devel
This package contains the development headers for QtQmlDevTools



#### Small plugin and import packages

%package import-etcprovider
Summary:    Qt Declarative etcprovider plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description import-etcprovider
This package provides the QtDeclarative etcprovider plugin

%package import-folderlistmodel
Summary:    Qt Declarative folderlistmodel plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description import-folderlistmodel
This package provides the QtDeclarative folderlistmodel plugin

%package import-gestures
Summary:    Qt Declarative gestures plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description import-gestures
This package provides the QtDeclarative gestures plugin

#%package import-inputcontext
#Summary:    Qt Declarative input context plugin
#Group:      Qt/Qt
#Requires:   %{name} = %{version}-%{release}
#
#%description import-inputcontext
#This package provides the QtDeclarative input context plugin

%package import-particles
Summary:    Qt Declarative particles plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description import-particles
This package provides the QtDeclarative particles plugin

%package plugin-qmlinspector
Summary:    Qt Declarative QML inspector plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-qmlinspector
This package provides the QML inspector plugin

%package import-qt47plugin
Summary:    Qt Declarative Qt 4.7 legacy support plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description import-qt47plugin
This package provides the legacy Qt 4.7 support plugin

%package import-qtquick1plugin
Summary:    Qt Declarative legacy QtQuick 1 support plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description import-qtquick1plugin
This package provides the legacy QtQuick 1 support plugin


%package import-qttest
Summary:    Qt Declarative QtTest plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description import-qttest
This package provides the QtDeclarative QtTest plugin

%package qmlviewer
Summary:    QML viewer
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description qmlviewer
This package contains the QML viewer for QtQuick 1.0 files.

%package qmlscene
Summary:    QML viewer
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
%setup -q -n %{name}
%patch0 -p1
%patch10 -p1


%build
export QTDIR=/usr/share/qt5
qmake
make %{?_smp_flags}

%install
rm -rf %{buildroot}
%make_install
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

%post qtquick1
/sbin/ldconfig
%postun qtquick1
/sbin/ldconfig







#### File section


%files
%defattr(-,root,root,-)
%{_libdir}/libQtDeclarative.so.5
%{_libdir}/libQtDeclarative.so.5.*

# FIXME: the provided .pc file is empty!
# Find out what gives and find a clean resolution
%files devel
%defattr(-,root,root,-)
%{_libdir}/libQtDeclarative.so
%{_libdir}/libQtDeclarative.prl
%{_libdir}/pkgconfig/QtDeclarative.pc
%{_includedir}/qt5/Qt/qdecl*.h
%{_includedir}/qt5/Qt/qtdecl*.h
%{_includedir}/qt5/Qt/qsg*.h
%{_includedir}/qt5/Qt/qjs*.h
%{_includedir}/qt5/Qt/qquick*.h
%{_includedir}/qt5/Qt/designersupport.h
%{_includedir}/qt5/Qt/QtDeclarative
%{_includedir}/qt5/QtDeclarative/
%{_datadir}/qt5/mkspecs/modules/qt_declarative.pri

%files qtquick1
%defattr(-,root,root,-)
%{_libdir}/libQtQuick1.so.5
%{_libdir}/libQtQuick1.so.5.*

%files qtquick1-devel
%defattr(-,root,root,-)
%{_libdir}/libQtQuick1.so
%{_libdir}/pkgconfig/QtQuick1.pc
%{_includedir}/qt5/Qt/qtquick1version.h
%{_includedir}/qt5/Qt/QtQuick1
%{_includedir}/qt5/QtQuick1/
%{_datadir}/qt5/mkspecs/modules/qt_qtquick1.pri






%files qmlviewer
%defattr(-,root,root,-)
%{_bindir}/qmlviewer

%files qmlscene
%defattr(-,root,root,-)
%{_bindir}/qmlscene

%files devel-tools
%defattr(-,root,root,-)
%{_bindir}/qmlplugindump
%{_bindir}/qmltestrunner
%{_bindir}/qmlmin



%files import-etcprovider
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/Qt/labs/etcprovider/*

%files import-folderlistmodel
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/Qt/labs/folderlistmodel/*

%files import-gestures
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/Qt/labs/gestures/*

#%files import-inputcontext
#%defattr(-,root,root,-)
#%{_libdir}/qt5/imports/Qt/labs/inputcontext/*

%files import-particles
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/Qt/labs/particles/*

%files plugin-qmlinspector
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/qmltooling/*

%files import-qttest
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/QtTest/

%files import-qt47plugin
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/Qt/

%files import-qtquick1plugin
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/QtQuick/





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
%{_libdir}/pkgconfig/QtQuickTest.pc
%{_datadir}/qt5/mkspecs/modules/qt_qmltest.pri

%files qtqmltools-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/QtQmlDevTools
%{_includedir}/qt5/QtQmlDevTools/
%{_libdir}/pkgconfig/QtQmlDevTools.pc
%{_datadir}/qt5/mkspecs/modules/qt_qmldevtools.pri









#### No changelog section, separate $pkg.changelog contains the history
