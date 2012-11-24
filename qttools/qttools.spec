%define _qtmodule_snapshot_version %nil
Name:       qt5-qttools
Summary:    Development tools for Qt
Version:    %{_qtmodule_snapshot_version}
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source:     %{name}-%{version}.tar.gz
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtsql-devel
BuildRequires:  qt5-qtxml-devel
BuildRequires:  qt5-qtdbus-devel
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qtprintsupport-devel
BuildRequires:  qt5-qmake
BuildRequires:  qt5-tools
BuildRequires:  fdupes
BuildRequires:  python

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains additional tools for building Qt applications.

%package devel
Summary:        Qt Tools - development files
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains development files for building against these
development tools. Most likely useful only when extending QtDesigner.

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
# Fix wrong path in pkgconfig files
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
-exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;
#
%fdupes %{buildroot}/%{_includedir}
%fdupes %{buildroot}/%{_libdir}/cmake


#### Pre/Post section

%post
/sbin/ldconfig
%postun
/sbin/ldconfig



%files
%defattr(-,root,root,-)
%{_bindir}/assistant
%{_bindir}/designer
%{_bindir}/lconvert
%{_bindir}/linguist
%{_bindir}/lrelease
%{_bindir}/lupdate
%{_bindir}/pixeltool
%{_bindir}/qcollectiongenerator
%{_bindir}/qdbus
%{_bindir}/qdbusviewer
%{_bindir}/qhelpconverter
%{_bindir}/qhelpgenerator
%{_libdir}/libQt*.so.5
%{_libdir}/libQt*.so.5.*
%{_datadir}/qt5/phrasebooks/

%files devel
%defattr(-,root,root,-)
%{_includedir}/qt5/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/*.prl
%{_libdir}/cmake/
%{_libdir}/pkgconfig/
%{_datadir}/qt5/mkspecs/modules/qt_lib_clucene.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_designer.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_designercomponents.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_help.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_uitools.pri


#### No changelog section, separate $pkg.changes contains the history

