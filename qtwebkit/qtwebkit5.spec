%define _qtmodule_snapshot_version %nil
%define _qtmodule_base_name qtwebkit

Name:       qt5-%{_qtmodule_base_name}
Summary:    Web content engine library for Qt
Version:    %{_qtmodule_snapshot_version}
Release:    1%{?dist}
Group:      Qt/Qt
License:    BSD and LGPLv2+
#URL:        http://trac.webkit.org/wiki/QtWebKit
URL:        https://gitorious.org/+qtwebkit-developers/webkit/qtwebkit/commits/qtwebkit-2.2
Source0:    %{name}-%{version}.tar.gz
Patch1:     0001-Fix-graphics-context-build.patch
Patch2:     0002-Fix-install-targets.patch
Patch3:     0003-Turn-developer-build-checking-off.patch
Patch4:     0004-Remove-tests-from-build.patch
Patch5:     0005-Do-not-build-tools.patch
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qtprintsupport-devel
BuildRequires:  qt5-qtlocation-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtv8-devel
BuildRequires:  qt5-qtqml-devel
BuildRequires:  qt5-qtqml-qtquick-devel
BuildRequires:  qt5-qt3d-devel
BuildRequires:  qt5-qtsensors-devel
BuildRequires:  qt5-qtxmlpatterns-devel
BuildRequires:  qt5-qmake
BuildRequires:  qt5-qtsql-devel
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  glib2-devel
BuildRequires:  gst-plugins-base-devel
BuildRequires:  gstreamer-devel
BuildRequires:  gperf
BuildRequires:  python
BuildRequires:  bison
BuildRequires:  fdupes


%description
QtWebKit provides a Web browser engine that makes it easy to embed content from
the World Wide Web into your Qt application.


%package uiprocess-launcher
Summary:    Web content engine library for Qt - WebKit2 process launcher
Group:      Qt/Qt

%description uiprocess-launcher
QtWebKit provides a Web browser engine that makes it easy to embed content from
the World Wide Web into your Qt application.

This package contains the UI process launcher for WebKit2 engine


%package -n lib%{_qtmodule_base_name}5
Summary:    Web content engine library for Qt - runtime files
Group:      Qt/Qt
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n lib%{_qtmodule_base_name}5
QtWebKit provides a Web browser engine that makes it easy to embed content from
the World Wide Web into your Qt application.

This package contains the runtime files needed to launch Qt 5 applications
using QtWebKit library.


%package -n lib%{_qtmodule_base_name}-devel
Summary:    Web content engine library for Qt - development files
Group:      Qt/Qt
Requires:   lib%{_qtmodule_base_name}5 = %{version}
Requires:   qt5-qtgui-devel >= 5~5.0.0

%description -n lib%{_qtmodule_base_name}-devel
QtWebKit provides a Web browser engine that makes it easy to embed content from
the World Wide Web into your Qt application.

This package contains the development files needed to build Qt 5 applications
using QtWebKit library.


%package -n qt5-qtqml-import-webkitplugin
Summary:    Qt WebKit QML plugin
Group:      Qt/Qt

%description -n qt5-qtqml-import-webkitplugin
QtWebKit provides a Web browser engine that makes it easy to embed content from
the World Wide Web into your Qt application.

This package contains the WebKit QML plugin for QtQml.


%package -n qt5-qtqml-import-webkitplugin-experimental
Summary:    Qt WebKit QML plugin (experimental)
Group:      Qt/Qt

%description -n qt5-qtqml-import-webkitplugin-experimental
QtWebKit provides a Web browser engine that makes it easy to embed content from
the World Wide Web into your Qt application.

This package contains the experimental WebKit QML plugin for QtQml.



%prep
%setup -q -n %{name}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
# remove .../qt/tests directory which introduces nothing but trouble
rm -rf Source/WebKit/qt/tests/

%build
# From Carsten Munk: create way smaller debuginfo
export CXXFLAGS="`echo $CXXFLAGS | sed 's/ -g / -gstabs /g'`"
export CFLAGS="`echo $CFLAGS | sed 's/ -g / -gstabs /g'`"
export QMAKEPATH="`pwd`/Tools/qmake"
export QTDIR=/usr/share/qt5
qmake  \
    CONFIG+=disable_uitools \
    DEFINES+=ENABLE_VIDEO=1 \
    DEFINES+=DISABLE_GEOLOCATION \
    DEFINES+=ENABLE_NETSCAPE_PLUGIN_API=0 \
    DEFINES+=ENABLE_ORIENTATION_EVENTS=0 \
    DEFINES+=ENABLE_DEVICE_ORIENTATION=0 \
    DEFINES+=WTF_USE_MOBILITY_SYSTEMINFO=0 \
    DEFINES+=ENABLE_JIT=1 \
    DEFINES+=ENABLE_WEBGL=0 \
    DEFINES+=WTF_ENABLE_GLIB_SUPPORT=1 \
    DEFINES+=ENABLE_GLIB_SUPPORT=1 \
    DEFINES+=WTF_USE_GSTREAMER=1

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%qmake_install
# Remove .la file
rm -f %{buildroot}/usr/lib/libQtWebKit.la
# Fix wrong path in pkgconfig files
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
-exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;
# Eliminate duplicates
%fdupes %{buildroot}/%{_libdir}
%fdupes %{buildroot}/%{_includedir}







%post -n lib%{_qtmodule_base_name}5 -p /sbin/ldconfig

%postun -n lib%{_qtmodule_base_name}5 -p /sbin/ldconfig








%files uiprocess-launcher
%defattr(-,root,root,-)
%{_bindir}/QtWebProcess


%files -n lib%{_qtmodule_base_name}5
%defattr(-,root,root,-)
%{_libdir}/libQtWebKit.so.*

%files -n lib%{_qtmodule_base_name}-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/*.h
%{_includedir}/qt5/Qt/QtWebKit
%{_includedir}/qt5/QtWebKit/
%{_libdir}/cmake/Qt5WebKit/
%{_libdir}/libQtWebKit.prl
%{_libdir}/libQtWebKit.so
%{_libdir}/pkgconfig/QtWebKit.pc
%{_datadir}/qt5/mkspecs/modules/qt_webkit.pri

%files -n qt5-qtqml-import-webkitplugin
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/QtWebKit/libqmlwebkitplugin.so
%{_libdir}/qt5/imports/QtWebKit/qmldir

%files -n qt5-qtqml-import-webkitplugin-experimental
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/QtWebKit/experimental/



#### No changelog section, separate $pkg.changes contains the history

