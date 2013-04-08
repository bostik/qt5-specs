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
Patch1:     0001-Remove-tests-from-build.patch
Patch2:		0002-Use-symbol-filter-when-linking.patch
Patch3:		0003-Try-to-force-shared-libs.patch
Patch4:		0004-Use-gold-linker-if-available.patch
Patch5:		0005-Disable-tools-entirely.patch
Patch6:		0006-Fix-case-insensitive-library-names.patch
Patch7:		0007-Drop-large-webkit-components-from-build.patch
Patch8:		0008-Add-build-options-to-WebKit.pro.patch
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qtprintsupport-devel
#BuildRequires:  qt5-qtlocation-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtv8-devel
BuildRequires:  qt5-qtqml-devel
BuildRequires:  qt5-qtqml-qtquick-devel
#BuildRequires:  qt5-qt3d-devel
#BuildRequires:  qt5-qtsensors-devel
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
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  gperf
BuildRequires:  python
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  fdupes
BuildRequires:  ruby


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
Summary:    Web content engine library for Qt - core runtime files
Group:      Qt/Qt
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n lib%{_qtmodule_base_name}5
QtWebKit provides a Web browser engine that makes it easy to embed content from
the World Wide Web into your Qt application.

This package contains the core runtime files needed to launch Qt 5 applications
using QtWebKit library.


%package -n lib%{_qtmodule_base_name}-devel
Summary:    Web content engine library for Qt - core development files
Group:      Qt/Qt
Requires:   lib%{_qtmodule_base_name}5 = %{version}

%description -n lib%{_qtmodule_base_name}-devel
QtWebKit provides a Web browser engine that makes it easy to embed content from
the World Wide Web into your Qt application.

This package contains the core development files needed to build Qt 5 applications
using QtWebKit library.


%package -n lib%{_qtmodule_base_name}5-widgets
Summary:    Web content engine library for Qt - GUI runtime files
Group:      Qt/Qt
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n lib%{_qtmodule_base_name}5-widgets
QtWebKit provides a Web browser engine that makes it easy to embed content from
the World Wide Web into your Qt application.

This package contains the GUI runtime files needed to launch Qt 5 applications
using QtWebKitWidgets library.


%package -n lib%{_qtmodule_base_name}-widgets-devel
Summary:    Web content engine library for Qt - GUI development files
Group:      Qt/Qt
Requires:   lib%{_qtmodule_base_name}5-widgets = %{version}

%description -n lib%{_qtmodule_base_name}-widgets-devel
QtWebKit provides a Web browser engine that makes it easy to embed content from
the World Wide Web into your Qt application.

This package contains the GUI development files needed to build Qt 5 applications
using QtWebKitWidgets library.


%package -n qt5-qtqml-import-webkitplugin
Summary:    Qt WebKit QML plugin
Group:      Qt/Qt

%description -n qt5-qtqml-import-webkitplugin
QtWebKit provides a Web browser engine that makes it easy to embed content from
the World Wide Web into your Qt application.

This package contains the WebKit QML plugin for QtQml.

%package -n qt5-qtqml-import-webkitplugin-experimental
Summary:    Qt WebKit Experimental QML plugin
Group:      Qt/Qt

%description -n qt5-qtqml-import-webkitplugin-experimental
QtWebKit provides a Web browser engine that makes it easy to embed content from
the World Wide Web into your Qt application.

This package contains the WebKit QML Experimental plugin for QtQml.


%prep
%setup -q -n %{name}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
# remove .../qt/tests directory which introduces nothing but trouble
rm -rf Source/WebKit/qt/tests/

%build
## From Carsten Munk: create way smaller debuginfo
#export CXXFLAGS="`echo $CXXFLAGS | sed 's/ -g / -gdwarf-4 /g'`"
#export CFLAGS="`echo $CFLAGS | sed 's/ -g / -gdwarf-4 /g'`"
# XXX: Remove debug symbols entirely, we're running out of linker memory!
export CXXFLAGS="`echo $CXXFLAGS | sed 's/ -g //g'`"
export CFLAGS="`echo $CFLAGS | sed 's/ -g //g'`"
#
export QMAKEPATH="`pwd`/Tools/qmake"
export QTDIR=/usr/share/qt5
# XXX: Dirty trick to use gold linker
# XXX: may work on x86 builds only(!)
%ifarch i586
mkdir /tmp/gold
cp /usr/bin/ld.gold /tmp/gold/ld
export PATH=/tmp/gold:$PATH
%endif
#
qmake
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%qmake_install
# Remove .la files
rm -f %{buildroot}/usr/lib/libQt5WebKit.la
rm -f %{buildroot}/usr/lib/libQt5WebKitWidgets.la
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

%post -n lib%{_qtmodule_base_name}5-widgets -p /sbin/ldconfig

%postun -n lib%{_qtmodule_base_name}5-widgets -p /sbin/ldconfig







%files uiprocess-launcher
%defattr(-,root,root,-)
%{_libdir}/qt5/libexec/QtWebProcess


%files -n lib%{_qtmodule_base_name}5
%defattr(-,root,root,-)
%{_libdir}/libQt5WebKit.so.*

%files -n lib%{_qtmodule_base_name}-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtWebKit/
%{_libdir}/cmake/Qt5WebKit/
%{_libdir}/libQt5WebKit.prl
%{_libdir}/libQt5WebKit.so
%{_libdir}/pkgconfig/Qt5WebKit.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_webkit.pri

%files -n lib%{_qtmodule_base_name}5-widgets
%defattr(-,root,root,-)
%{_libdir}/libQt5WebKitWidgets.so.*

%files -n lib%{_qtmodule_base_name}-widgets-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtWebKitWidgets/
%{_libdir}/cmake/Qt5WebKitWidgets/
%{_libdir}/libQt5WebKitWidgets.prl
%{_libdir}/libQt5WebKitWidgets.so
%{_libdir}/pkgconfig/Qt5WebKitWidgets.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_webkitwidgets.pri

%files -n qt5-qtqml-import-webkitplugin
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtWebKit/libqmlwebkitplugin.so
%{_libdir}/qt5/qml/QtWebKit/qmldir

%files -n qt5-qtqml-import-webkitplugin-experimental
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtWebKit/experimental/libqmlwebkitexperimentalplugin.so
%{_libdir}/qt5/qml/QtWebKit/experimental/qmldir


#### No changelog section, separate $pkg.changes contains the history

