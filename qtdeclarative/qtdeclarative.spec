Name:       qt5-declarative
Summary:    Qt Declarative library
Version:    4.9.90.20110701+g5b84efd6
Release:    1%{?dist}
Group:      System/Libraries
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}.tar.gz
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qtopengl-devel
BuildRequires:  qt5-qtsql-devel
BuildRequires:  qt5-qttest-devel
BuildRequires:  qt5-script-devel
BuildRequires:  qt5-qmake
BuildRequires:  fontconfig-devel
BuildRequires:  fdupes

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Declarative library


%package devel
Summary:    Qt Declarative - development files
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Declarative library development files

%package qtquicktest
Summary:    Qt Declarative QtQuickTest library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtquicktest
This package contains the QtQuickTest library for QtDeclarative module

%package qtquicktest-devel
Summary:    Qt Declarative QtQuickTest - development files
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-devel = %{version}-%{release}
Requires:   qt5-declarative-qtquicktest = %{version}-%{release}

%description qtquicktest-devel
This package contains the development headers for QtQuickTest library


#### Small plugin and import packages

%package import-etcprovider
Summary:    Qt Declarative etcprovider plugin
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description import-etcprovider
This package provides the QtDeclarative etcprovider plugin

%package import-folderlistmodel
Summary:    Qt Declarative folderlistmodel plugin
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description import-folderlistmodel
This package provides the QtDeclarative folderlistmodel plugin

%package import-gestures
Summary:    Qt Declarative gestures plugin
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description import-gestures
This package provides the QtDeclarative gestures plugin

%package import-inputcontext
Summary:    Qt Declarative input context plugin
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description import-inputcontext
This package provides the QtDeclarative input context plugin

%package import-particles
Summary:    Qt Declarative particles plugin
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description import-particles
This package provides the QtDeclarative particles plugin

%package plugin-qmlinspector
Summary:    Qt Declarative QML inspector plugin
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description plugin-qmlinspector
This package provides the QML inspector plugin

%package import-qttest
Summary:    Qt Declarative QtTest plugin
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description import-qttest
This package provides the QtDeclarative QtTest plugin

%package qmlviewer
Summary:    QML viewer
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}

%description qmlviewer
This package contains the QML viewer for QtQuick 1.0 files.

%package qmlscene
Summary:    QML viewer
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}

%description qmlscene
This package contains the QML viewer for QtQuick 2.0 files.

%package devel-tools
Summary:    QML development tools
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}

%description devel-tools
This package contains QML debugging and development tools







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
%fdupes %{_buildroot}/%{_libdir}
%fdupes %{_buildroot}/%{_includedir}




#### Pre/Post section

%post
/sbin/ldconfig
%postun
/sbin/ldconfig

%post qtquicktest
/sbin/ldconfig
%postun qtquicktest
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
%{_libdir}/pkgconfig/*
%{_includedir}/qt5/Qt/qdecl*.h
%{_includedir}/qt5/Qt/qsg*.h
%{_includedir}/qt5/Qt/QtDeclarative
%{_includedir}/qt5/QtDeclarative/
%{_datadir}/qt5/mkspecs/modules/qt_declarative.pri

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



%files import-etcprovider
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/Qt/labs/etcprovider/*

%files import-folderlistmodel
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/Qt/labs/folderlistmodel/*

%files import-gestures
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/Qt/labs/gestures/*

%files import-inputcontext
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/Qt/labs/inputcontext/*

%files import-particles
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/Qt/labs/particles/*

%files plugin-qmlinspector
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/qmltooling/*

%files import-qttest
%{_libdir}/qt5/imports/QtTest/
%defattr(-,root,root,-)


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
%{_libdir}/qt5/mkspecs/modules/qt_qmltest.pri








#### Changelog section

%changelog
* Tue Jul  5 2011 Mika Boström <mika.bostrom@nomovok.com> - 4.9.90.20110701
- Split into more packages
- Create packages for all imports and plugins
* Mon Jul  4 2011 Mika Boström <mika.bostrom@nomovok.com> - 4.9.90.20110701
- Initial packaging
- Builds against packages from qtbase build

