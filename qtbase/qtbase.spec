%ifarch arvm7l armv7el armv7hl amv7nhl armv7thl armv7tnhl
%define arch_arg armv6
%endif
%ifarch i586
%define arch_arg i386
%endif


# Version is the date of latest commit in qtbase, followed by 'g' + few
# characters of the last git commit ID.
# NOTE: tarball's prefix is 'qt5-base' until version number starts to
# make sense. This allows to update spec contents easily as snapshots
# evolve.

Name:       qt5
Summary:    Cross-platform application and UI framework
Version:    4.9.90.20110628+g6fa15d7
Release:    1%{?dist}
Group:      System/Libraries
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-base.tar.gz
Source1:    macros.qmake
Patch0:     eglfs-must-dep-on-egl.patch
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  cups-devel
BuildRequires:  fdupes
BuildRequires:  flex
# Package not available but installed in OBS?
#BuildRequires:  gcc-g++
BuildRequires:  libjpeg-devel
BuildRequires:  libmng-devel
BuildRequires:  libtiff-devel
BuildRequires:  pam-devel
BuildRequires:  readline-devel
BuildRequires:  sharutils


%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.


%package tools
Summary:    Development tools for qtbase
Group:      Development/Tools

%description tools
This package contains useful tools for Qt development

%package qtcore
Summary:    The QtCore library
Group:      Development/library
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtcore
This packagea contains the QtCore library

%package qtcore-devel
Summary:    Development files for QtCore
Group:      Development/Libraries
Requires:   %{name}-qmake
Requires:   %{name}-tools
Requires:   %{name}-qtcore = %{version}-%{release}

%description qtcore-devel
This package contains the files necessary to develop applications
that use the QtCore


%package qmake
Summary:    QMake
Group:      Development/Tools

%description qmake
This package contains qmake


%package plugin-accessible-libqtaccessiblewidgets
Summary:    Accessible widgets
Group:      Development/Libraries

%description plugin-accessible-libqtaccessiblewidgets
This package contains libqtaccessiblewidgets


%package plugin-bearer-connman
Summary:    Connman bearer plugin
Group:      Development/Libraries

%description plugin-bearer-connman
This package contains the connman bearer plugin


%package plugin-bearer-generic
Summary:    Connman generic plugin
Group:      Development/Libraries

%description plugin-bearer-generic
This package contains the connman generic bearer plugin


%package plugin-bearer-nm
Summary:    Connman generic plugin
Group:      Development/Libraries

%description plugin-bearer-nm
This package contains the connman NetworkManager bearer plugin


%package plugin-imageformat-gif
Summary:    Gif image format plugin
Group:      Development/Libraries

%description plugin-imageformat-gif
This package contains the gif imageformat plugin


%package plugin-imageformat-ico
Summary:    Ico image format plugin
Group:      Development/Libraries

%description plugin-imageformat-ico
This package contains the ico imageformat plugin


%package plugin-imageformat-jpeg
Summary:    JPEG image format plugin
Group:      Development/libraries

%description plugin-imageformat-jpeg
This package contains the JPEG imageformat plugin


%package plugin-imageformat-mng
Summary:    MNG image format plugin
Group:      Development/libraries

%description plugin-imageformat-mng
This package contains the MNG imageformat plugin


%package plugin-imageformat-tiff
Summary:    TIFF image format plugin
Group:      Development/libraries

%description plugin-imageformat-tiff
This package contains the TIFF imageformat plugin


%package plugin-platform-minimal
Summary:    Minimal platform plugin
Group:      Development/Libraries

%description plugin-platform-minimal
This package contains the minimal platform plugin


%package plugin-platform-wayland
Summary:    Wayland platform plugin
Group:      Development/Libraries

%description plugin-platform-wayland
This package contains the wayland platform plugin


%package plugin-platform-eglfs
Summary:    Eglfs platform plugin
Group:      Development/Libraries

%description plugin-platform-eglfs
This package contains the eglfs platform plugin


%package plugin-sqldriver-sqlite
Summary:    Sqlite sql driver plugin
Group:      Development/Libraries

%description plugin-sqldriver-sqlite
This package contains the sqlite sql driver plugin


%package plugin-inputmethod-imsw-multi
Summary:    imsw-multi input method
Group:      Development/Libraries

%description plugin-inputmethod-imsw-multi
This package contains the imsw-multi input method plugin





%package qtdbus
Summary:    The QtDBus library
Group:      Development/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtdbus
This package contains the QtDBus library


%package qtdbus-devel
Summary:    Development files for QtDBus
Group:      Development/Libraries
Requires:   %{name}-qtdbus = %{version}-%{release}

%description qtdbus-devel
This package contains the files necessary to develop
applications that use QtDBus


%package qtgui
Summary:    The QtGuji Library
Group:      Development/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtgui
This package contains the QtGui library


%package qtgui-devel
Summary:    Development files for QtGui
Group:      Development/Libraries
Requires:   %{name}-qtgui = %{version}-%{release}

%description qtgui-devel
This package contains the files necessary to develop
applications that use QtGui


%package qtnetwork
Summary:    The QtNetwork library
Group:      Development/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtnetwork
This package contains the QtNetwork library


%package qtnetwork-devel
Summary:    Development files for QtNetwork
Group:      Development/Libraries
Requires:   %{name}-qtnetwork = %{version}-%{release}

%description qtnetwork-devel
This package contains the files necessary to develop
applications that use QtNetwork



%package qtopengl
Summary:    The QtOpenGL library
Group:      Development/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtopengl
This package contains the QtOpenGL library


%package qtopengl-devel
Summary:    Development files for QtOpenGL
Group:      Development/Libraries
Requires:   %{name}-qtopengl = %{version}-%{release}
Requires:   libGLESv2-devel
Requires:   libEGL-devel

%description qtopengl-devel
This package contains the files necessary to develop
applications that use QtOpenGL


%package qtsql
Summary:    The QtSql library
Group:      Development/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtsql
This package contains the QtSql library


%package qtsql-devel
Summary:    Development files for QtSql
Group:      Development/Libraries
Requires:   %{name}-qtsql = %{version}-%{release}

%description qtsql-devel
This package contains the files necessary to develop
applications that use QtSql


%package qttest
Summary:    The QtTest library
Group:      Development/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qttest
This package contains the QtTest library


%package qttest-devel
Summary:    Development files for QtTest
Group:      Development/Libraries
Requires:   %{name}-qttest = %{version}-%{release}

%description qttest-devel
This package contains the files necessary to develop
applications that use QtTest


%package qtxml
Summary:    The QtXml library
Group:      Development/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtxml
This package contains the QtXml library

%package qtxml-devel
Summary:    Development files for QtXml
Group:      Development/Libraries
Requires:   %{name}-qtxml = %{version}-%{release}

%description qtxml-devel
This package contains the files necessary to develop
applications that use QtXml



#%package qtuitools
#Summary:    The QtUiTools library
#Group:      Development/Libraries
#Requires:   %{name} = %{version}-%{release}
#Requires(post):     /sbin/ldconfig
#Requires(postun):   /sbin/ldconfig
#
#%description qtuitools
#This package contains the QtUiTools library

%package qtuitools-devel
Summary:    Development files for QtUiTools
Group:      Development/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtuitools-devel
This package contains the files necessary to develop
applications that use QtUiTools

%package qtdesigner-devel
Summary:    Development files for QtDesigner
Group:      Development/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtdesigner-devel
This package contains the files necessary to develop
applications that use QtDesigner




##### Build section

%prep
%setup -q -n %{name}-base
%patch0 -p2


%build
export QT_WAYLAND_GL_CONFIG=wayland_egl
echo "SUBDIRS += eglfs" >> src/plugins/platforms/platforms.pro
#
./configure --disable-static \
    -confirm-license \
    -developer-build \
    -platform linux-g++ \
    -prefix "%{_prefix}" \
    -bindir "%{_bindir}" \
    -libdir "%{_libdir}" \
    -docdir "%{_docdir}" \
    -headerdir "%{_includedir}/qt5" \
    -datadir "%{_datadir}/qt5" \
    -plugindir "%{_libdir}/qt5/plugins" \
    -importdir "%{_libdir}/qt5/imports" \
    -translationdir "%{_datadir}/qt5/translations" \
    -sysconfdir "%{_sysconfdir}/xdg" \
    -examplesdir "%{_libdir}/qt5/examples" \
    -opensource \
    -no-sql-ibase \
    -no-sql-mysql \
    -no-sql-odbc \
    -no-sql-psql \
    -plugin-sql-sqlite \
    -no-sql-sqlite2 \
    -no-sql-tds \
    -system-sqlite \
    -no-qt3support \
    -no-xmlpatterns \
    -no-multimedia \
    -audio-backend \
    -phonon \
    -no-phonon-backend \
    -no-svg \
    -no-webkit \
    -no-script \
    -no-scripttools \
    -system-zlib \
    -system-libtiff \
    -system-libpng \
    -system-libjpeg \
    -no-rpath \
    -optimized-qmake \
    -dbus-linked \
    -no-separate-debug-info \
    -verbose \
    -no-gtkstyle \
    -no-nas-sound \
    -opengl es2 \
    -arch %{arch_arg} \
    -no-openvg \
    -lfontconfig \
    -I/usr/include/freetype2 \
    -no-neon \
    -nomake tests \
    -nomake examples \
    -nomake demos \
    -qpa
#
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
#
# Fix wrong path in pkgconfig files
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
-exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;
#
# Install qmake rpm macros
install -D -p -m 0644 %{_sourcedir}/macros.qmake \
%{buildroot}/%{_sysconfdir}/rpm/macros.qmake
#
# Install a dummy file for "naked" qt5 package
echo "Qt5 package does not contain anything by itself" > /tmp/qt5.txt
install -D -p -m 0644 /tmp/qt5.txt \
%{buildroot}/%{_datadir}/doc/%{name}/qt5.txt
#
%fdupes %{buildroot}/%{_libdir}
%fdupes %{buildroot}/%{_includedir}
%fdupes %{buildroot}/%{_datadir}


#### Pre/Post section

%post qtcore -p /sbin/ldconfig
%postun qtcore -p /sbin/ldconfig

%post qtdbus -p /sbin/ldconfig
%postun qtdbus -p /sbin/ldconfig

%post qtsql -p /sbin/ldconfig
%postun qtsql -p /sbin/ldconfig

%post qtnetwork -p /sbin/ldconfig
%postun qtnetwork -p /sbin/ldconfig

%post qtgui -p /sbin/ldconfig
%postun qtgui -p /sbin/ldconfig

%post qttest -p /sbin/ldconfig
%postun qttest -p /sbin/ldconfig

%post qtopengl -p /sbin/ldconfig
%postun qtopengl -p /sbin/ldconfig

%post qtxml -p /sbin/ldconfig
%postun qtxml -p /sbin/ldconfig





#### File section

# There is no naked qt5 package
#%files



%files tools
%defattr(-,root,root,-)
%{_bindir}/moc
%{_bindir}/rcc
%{_bindir}/syncqt
%{_bindir}/uic


%files qtcore
%defattr(-,root,root,-)
%{_libdir}/libQtCore.so.5
%{_libdir}/libQtCore.so.5.*

%files qtcore-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/QtCore
%{_includedir}/qt5/QtCore/
%{_includedir}/qt5/Qt/qatomic_*.h
%{_includedir}/qt5/Qt/qconfig.h
%{_includedir}/qt5/Qt/qconfig-*.h
%{_includedir}/qt5/Qt/qfunctions_*.h
%{_includedir}/qt5/Qt/qtcoreversion.h
%{_includedir}/qt5/Qt/qabstractfileengine.h
%{_includedir}/qt5/Qt/qbuffer.h
%{_includedir}/qt5/Qt/qdatastream.h
%{_includedir}/qt5/Qt/qdebug.h
%{_includedir}/qt5/Qt/qdir.h
%{_includedir}/qt5/Qt/qdiriterator.h
%{_includedir}/qt5/Qt/qfile.h
%{_includedir}/qt5/Qt/qfileinfo.h
%{_includedir}/qt5/Qt/qfilesystemwatcher.h
%{_includedir}/qt5/Qt/qfsfileengine.h
%{_includedir}/qt5/Qt/qiodevice.h
%{_includedir}/qt5/Qt/qprocess.h
%{_includedir}/qt5/Qt/qresource.h
%{_includedir}/qt5/Qt/qsettings.h
%{_includedir}/qt5/Qt/qtemporaryfile.h
%{_includedir}/qt5/Qt/qtextstream.h
%{_includedir}/qt5/Qt/qurl.h
%{_includedir}/qt5/Qt/qfuture.h
%{_includedir}/qt5/Qt/qfutureinterface.h
%{_includedir}/qt5/Qt/qfuturesynchronizer.h
%{_includedir}/qt5/Qt/qfuturewatcher.h
%{_includedir}/qt5/Qt/qrunnable.h
%{_includedir}/qt5/Qt/qtconcurrentcompilertest.h
%{_includedir}/qt5/Qt/qtconcurrentexception.h
%{_includedir}/qt5/Qt/qtconcurrentfilter.h
%{_includedir}/qt5/Qt/qtconcurrentfilterkernel.h
%{_includedir}/qt5/Qt/qtconcurrentfunctionwrappers.h
%{_includedir}/qt5/Qt/qtconcurrentiteratekernel.h
%{_includedir}/qt5/Qt/qtconcurrentmap.h
%{_includedir}/qt5/Qt/qtconcurrentmapkernel.h
%{_includedir}/qt5/Qt/qtconcurrentmedian.h
%{_includedir}/qt5/Qt/qtconcurrentreducekernel.h
%{_includedir}/qt5/Qt/qtconcurrentresultstore.h
%{_includedir}/qt5/Qt/qtconcurrentrun.h
%{_includedir}/qt5/Qt/qtconcurrentrunbase.h
%{_includedir}/qt5/Qt/qtconcurrentstoredfunctioncall.h
%{_includedir}/qt5/Qt/qtconcurrentthreadengine.h
%{_includedir}/qt5/Qt/qthreadpool.h
%{_includedir}/qt5/Qt/qfactoryinterface.h
%{_includedir}/qt5/Qt/qlibrary.h
%{_includedir}/qt5/Qt/qplugin.h
%{_includedir}/qt5/Qt/qpluginloader.h
%{_includedir}/qt5/Qt/quuid.h
%{_includedir}/qt5/Qt/qxmlstream.h
%{_includedir}/qt5/Qt/qabstractanimation.h
%{_includedir}/qt5/Qt/qanimationgroup.h
%{_includedir}/qt5/Qt/qparallelanimationgroup.h
%{_includedir}/qt5/Qt/qpauseanimation.h
%{_includedir}/qt5/Qt/qpropertyanimation.h
%{_includedir}/qt5/Qt/qsequentialanimationgroup.h
%{_includedir}/qt5/Qt/qvariantanimation.h
%{_includedir}/qt5/Qt/qendian.h
%{_includedir}/qt5/Qt/qfeatures.h
%{_includedir}/qt5/Qt/qglobal.h
%{_includedir}/qt5/Qt/qlibraryinfo.h
%{_includedir}/qt5/Qt/qnamespace.h
%{_includedir}/qt5/Qt/qnumeric.h
%{_includedir}/qt5/Qt/qalgorithms.h
%{_includedir}/qt5/Qt/qbitarray.h
%{_includedir}/qt5/Qt/qbytearray.h
%{_includedir}/qt5/Qt/qbytearraymatcher.h
%{_includedir}/qt5/Qt/qcache.h
%{_includedir}/qt5/Qt/qchar.h
%{_includedir}/qt5/Qt/qcontainerfwd.h
%{_includedir}/qt5/Qt/qcontiguouscache.h
%{_includedir}/qt5/Qt/qcryptographichash.h
%{_includedir}/qt5/Qt/qdatetime.h
%{_includedir}/qt5/Qt/qeasingcurve.h
%{_includedir}/qt5/Qt/qelapsedtimer.h
%{_includedir}/qt5/Qt/qhash.h
%{_includedir}/qt5/Qt/qiterator.h
%{_includedir}/qt5/Qt/qline.h
%{_includedir}/qt5/Qt/qlinkedlist.h
%{_includedir}/qt5/Qt/qlist.h
%{_includedir}/qt5/Qt/qlocale.h
%{_includedir}/qt5/Qt/qmap.h
%{_includedir}/qt5/Qt/qmargins.h
%{_includedir}/qt5/Qt/qpair.h
%{_includedir}/qt5/Qt/qpoint.h
%{_includedir}/qt5/Qt/qqueue.h
%{_includedir}/qt5/Qt/qrect.h
%{_includedir}/qt5/Qt/qregexp.h
%{_includedir}/qt5/Qt/qscopedpointer.h
%{_includedir}/qt5/Qt/qscopedvaluerollback.h
%{_includedir}/qt5/Qt/qset.h
%{_includedir}/qt5/Qt/qshareddata.h
%{_includedir}/qt5/Qt/qsharedpointer*.h
%{_includedir}/qt5/Qt/qsize.h
%{_includedir}/qt5/Qt/qstack.h
%{_includedir}/qt5/Qt/qstring.h
%{_includedir}/qt5/Qt/qstringbuilder.h
%{_includedir}/qt5/Qt/qstringlist.h
%{_includedir}/qt5/Qt/qstringmatcher.h
%{_includedir}/qt5/Qt/qtextboundaryfinder.h
%{_includedir}/qt5/Qt/qtimeline.h
%{_includedir}/qt5/Qt/qvarlengtharray.h
%{_includedir}/qt5/Qt/qvector.h
%{_includedir}/qt5/Qt/qatomic.h
%{_includedir}/qt5/Qt/qbasicatomic.h
%{_includedir}/qt5/Qt/qmutex.h
%{_includedir}/qt5/Qt/qreadwritelock.h
%{_includedir}/qt5/Qt/qsemaphore.h
%{_includedir}/qt5/Qt/qthread.h
%{_includedir}/qt5/Qt/qthreadstorage.h
%{_includedir}/qt5/Qt/qwaitcondition.h
%{_includedir}/qt5/Qt/qabstracteventdispatcher.h
%{_includedir}/qt5/Qt/qabstractitemmodel.h
%{_includedir}/qt5/Qt/qbasictimer.h
%{_includedir}/qt5/Qt/qcoreapplication.h
%{_includedir}/qt5/Qt/qcoreevent.h
%{_includedir}/qt5/Qt/qeventloop.h
%{_includedir}/qt5/Qt/qmath.h
%{_includedir}/qt5/Qt/qmetaobject.h
%{_includedir}/qt5/Qt/qmetatype.h
%{_includedir}/qt5/Qt/qmimedata.h
%{_includedir}/qt5/Qt/qobject.h
%{_includedir}/qt5/Qt/qobjectcleanuphandler.h
%{_includedir}/qt5/Qt/qobjectdefs.h
%{_includedir}/qt5/Qt/qpointer.h
%{_includedir}/qt5/Qt/qsharedmemory.h
%{_includedir}/qt5/Qt/qsignalmapper.h
%{_includedir}/qt5/Qt/qsocketnotifier.h
%{_includedir}/qt5/Qt/qsystemsemaphore.h
%{_includedir}/qt5/Qt/qtimer.h
%{_includedir}/qt5/Qt/qtranslator.h
%{_includedir}/qt5/Qt/qvariant.h
%{_includedir}/qt5/Qt/qtextcodec.h
%{_includedir}/qt5/Qt/qtextcodecplugin.h
%{_includedir}/qt5/Qt/qabstractstate.h
%{_includedir}/qt5/Qt/qabstracttransition.h
%{_includedir}/qt5/Qt/qeventtransition.h
%{_includedir}/qt5/Qt/qfinalstate.h
%{_includedir}/qt5/Qt/qhistorystate.h
%{_includedir}/qt5/Qt/qsignaltransition.h
%{_includedir}/qt5/Qt/qstate.h
%{_includedir}/qt5/Qt/qstatemachine.h
%{_includedir}/qt5/Qt/qt_windows.h
%{_libdir}/libQtCore.prl
%{_libdir}/libQtCore.so
%{_libdir}/pkgconfig/QtCore.pc
%{_datadir}/qt5/mkspecs/modules/qt_core.pri

%files qmake
%defattr(-,root,root,-)
%{_bindir}/qmake
%{_datadir}/qt5/mkspecs/aix-*/
%{_datadir}/qt5/mkspecs/common/
%{_datadir}/qt5/mkspecs/cygwin-*/
%{_datadir}/qt5/mkspecs/darwin-*/
%{_datadir}/qt5/mkspecs/default
%{_datadir}/qt5/mkspecs/features/
%{_datadir}/qt5/mkspecs/freebsd-*/
%{_datadir}/qt5/mkspecs/hpux-*
%{_datadir}/qt5/mkspecs/hpuxi-*
%{_datadir}/qt5/mkspecs/hurd-g++/
%{_datadir}/qt5/mkspecs/irix-*/
%{_datadir}/qt5/mkspecs/linux-*/
%{_datadir}/qt5/mkspecs/lynxos-*/
%{_datadir}/qt5/mkspecs/macx-*/
%{_datadir}/qt5/mkspecs/netbsd-*/
%{_datadir}/qt5/mkspecs/openbsd-*/
%{_datadir}/qt5/mkspecs/qconfig.pri
%{_datadir}/qt5/mkspecs/qmodule.pri
%{_datadir}/qt5/mkspecs/qws/
%{_datadir}/qt5/mkspecs/sco-*/
%{_datadir}/qt5/mkspecs/solaris-*/
%{_datadir}/qt5/mkspecs/symbian-*/
%{_datadir}/qt5/mkspecs/tru64-*/
%{_datadir}/qt5/mkspecs/unixware-*/
%{_datadir}/qt5/mkspecs/unsupported/
%{_datadir}/qt5/mkspecs/win32-borland/
%{_datadir}/qt5/mkspecs/win32-g++/
%{_datadir}/qt5/mkspecs/win32-icc/
%{_datadir}/qt5/mkspecs/win32-msvc20*/
%{_datadir}/qt5/mkspecs/wince*/
%{_sysconfdir}/rpm/macros.qmake

%files qtdbus
%defattr(-,root,root,-)
%{_libdir}/libQtDBus.so.5
%{_libdir}/libQtDBus.so.5.*


%files qtdbus-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/QtDBus
%{_includedir}/qt5/QtDBus/
%{_includedir}/qt5/Qt/qdbusabstractadaptor.h
%{_includedir}/qt5/Qt/qdbusabstractinterface.h
%{_includedir}/qt5/Qt/qdbusargument.h
%{_includedir}/qt5/Qt/qdbusconnection.h
%{_includedir}/qt5/Qt/qdbusconnectioninterface.h
%{_includedir}/qt5/Qt/qdbuscontext.h
%{_includedir}/qt5/Qt/qdbuserror.h
%{_includedir}/qt5/Qt/qdbusextratypes.h
%{_includedir}/qt5/Qt/qdbusinterface.h
%{_includedir}/qt5/Qt/qdbusmacros.h
%{_includedir}/qt5/Qt/qdbusmessage.h
%{_includedir}/qt5/Qt/qdbusmetatype.h
%{_includedir}/qt5/Qt/qdbuspendingcall.h
%{_includedir}/qt5/Qt/qdbuspendingreply.h
%{_includedir}/qt5/Qt/qdbusreply.h
%{_includedir}/qt5/Qt/qdbusserver.h
%{_includedir}/qt5/Qt/qdbusservicewatcher.h
%{_includedir}/qt5/Qt/qdbusunixfiledescriptor.h
%{_includedir}/qt5/Qt/qtdbusversion.h
%{_libdir}/libQtDBus.so
%{_libdir}/libQtDBus.prl
%{_libdir}/pkgconfig/QtDBus.pc
%{_datadir}/qt5/mkspecs/modules/qt_dbus.pri


%files qtgui
%defattr(-,root,root,-)
%{_libdir}/libQtGui.so.5
%{_libdir}/libQtGui.so.5.*


%files qtgui-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtGui/
%{_includedir}/qt5/Qt/QtGui
%{_includedir}/qt5/Qt/qabstractfontengine_qws.h
%{_includedir}/qt5/Qt/qtguiversion.h
%{_includedir}/qt5/Qt/qs60mainapplication.h
%{_includedir}/qt5/Qt/qs60mainappui.h
%{_includedir}/qt5/Qt/qs60maindocument.h
%{_includedir}/qt5/Qt/qgraphicseffect.h
%{_includedir}/qt5/Qt/qgenericmatrix.h
%{_includedir}/qt5/Qt/qmatrix4x4.h
%{_includedir}/qt5/Qt/qquaternion.h
%{_includedir}/qt5/Qt/qvector2d.h
%{_includedir}/qt5/Qt/qvector3d.h
%{_includedir}/qt5/Qt/qvector4d.h
%{_includedir}/qt5/Qt/qabstracttextdocumentlayout.h
%{_includedir}/qt5/Qt/qfont.h
%{_includedir}/qt5/Qt/qfontdatabase.h
%{_includedir}/qt5/Qt/qfontinfo.h
%{_includedir}/qt5/Qt/qfontmetrics.h
%{_includedir}/qt5/Qt/qglyphrun.h
%{_includedir}/qt5/Qt/qrawfont.h
%{_includedir}/qt5/Qt/qstatictext.h
%{_includedir}/qt5/Qt/qsyntaxhighlighter.h
%{_includedir}/qt5/Qt/qtextcursor.h
%{_includedir}/qt5/Qt/qtextdocument.h
%{_includedir}/qt5/Qt/qtextdocumentfragment.h
%{_includedir}/qt5/Qt/qtextdocumentwriter.h
%{_includedir}/qt5/Qt/qtextformat.h
%{_includedir}/qt5/Qt/qtextlayout.h
%{_includedir}/qt5/Qt/qtextlist.h
%{_includedir}/qt5/Qt/qtextobject.h
%{_includedir}/qt5/Qt/qtextoption.h
%{_includedir}/qt5/Qt/qtexttable.h
%{_includedir}/qt5/Qt/qinputcontext.h
%{_includedir}/qt5/Qt/qinputcontextfactory.h
%{_includedir}/qt5/Qt/qinputcontextplugin.h
%{_includedir}/qt5/Qt/qcompleter.h
%{_includedir}/qt5/Qt/qdesktopservices.h
%{_includedir}/qt5/Qt/qscroller.h
%{_includedir}/qt5/Qt/qscrollerproperties.h
%{_includedir}/qt5/Qt/qsystemtrayicon.h
%{_includedir}/qt5/Qt/qundogroup.h
%{_includedir}/qt5/Qt/qundostack.h
%{_includedir}/qt5/Qt/qundoview.h
%{_includedir}/qt5/Qt/qvfbhdr.h
%{_includedir}/qt5/Qt/qws*.h
%{_includedir}/qt5/Qt/qabstractbutton.h
%{_includedir}/qt5/Qt/qabstractscrollarea.h
%{_includedir}/qt5/Qt/qabstractslider.h
%{_includedir}/qt5/Qt/qabstractspinbox.h
%{_includedir}/qt5/Qt/qbuttongroup.h
%{_includedir}/qt5/Qt/qcalendarwidget.h
%{_includedir}/qt5/Qt/qcheckbox.h
%{_includedir}/qt5/Qt/qcombobox.h
%{_includedir}/qt5/Qt/qcommandlinkbutton.h
%{_includedir}/qt5/Qt/qdatetimeedit.h
%{_includedir}/qt5/Qt/qdial.h
%{_includedir}/qt5/Qt/qdialogbuttonbox.h
%{_includedir}/qt5/Qt/qdockwidget.h
%{_includedir}/qt5/Qt/qfocusframe.h
%{_includedir}/qt5/Qt/qfontcombobox.h
%{_includedir}/qt5/Qt/qframe.h
%{_includedir}/qt5/Qt/qgroupbox.h
%{_includedir}/qt5/Qt/qlabel.h
%{_includedir}/qt5/Qt/qlcdnumber.h
%{_includedir}/qt5/Qt/qlineedit.h
%{_includedir}/qt5/Qt/qmainwindow.h
%{_includedir}/qt5/Qt/qmdiarea.h
%{_includedir}/qt5/Qt/qmdisubwindow.h
%{_includedir}/qt5/Qt/qmenu.h
%{_includedir}/qt5/Qt/qmenubar.h
%{_includedir}/qt5/Qt/qmenudata.h
%{_includedir}/qt5/Qt/qplaintextedit.h
%{_includedir}/qt5/Qt/qprintpreviewwidget.h
%{_includedir}/qt5/Qt/qprogressbar.h
%{_includedir}/qt5/Qt/qpushbutton.h
%{_includedir}/qt5/Qt/qradiobutton.h
%{_includedir}/qt5/Qt/qrubberband.h
%{_includedir}/qt5/Qt/qscrollarea.h
%{_includedir}/qt5/Qt/qscrollbar.h
%{_includedir}/qt5/Qt/qsizegrip.h
%{_includedir}/qt5/Qt/qslider.h
%{_includedir}/qt5/Qt/qspinbox.h
%{_includedir}/qt5/Qt/qsplashscreen.h
%{_includedir}/qt5/Qt/qsplitter.h
%{_includedir}/qt5/Qt/qstackedwidget.h
%{_includedir}/qt5/Qt/qstatusbar.h
%{_includedir}/qt5/Qt/qtabbar.h
%{_includedir}/qt5/Qt/qtabwidget.h
%{_includedir}/qt5/Qt/qtextbrowser.h
%{_includedir}/qt5/Qt/qtextedit.h
%{_includedir}/qt5/Qt/qtoolbar.h
%{_includedir}/qt5/Qt/qtoolbox.h
%{_includedir}/qt5/Qt/qtoolbutton.h
%{_includedir}/qt5/Qt/qvalidator.h
%{_includedir}/qt5/Qt/qworkspace.h
%{_includedir}/qt5/Qt/qsymbianevent.h
%{_includedir}/qt5/Qt/qbitmap.h
%{_includedir}/qt5/Qt/qicon.h
%{_includedir}/qt5/Qt/qiconengine.h
%{_includedir}/qt5/Qt/qiconengineplugin.h
%{_includedir}/qt5/Qt/qimage.h
%{_includedir}/qt5/Qt/qimageiohandler.h
%{_includedir}/qt5/Qt/qimagereader.h
%{_includedir}/qt5/Qt/qimagewriter.h
%{_includedir}/qt5/Qt/qmovie.h
%{_includedir}/qt5/Qt/qpicture.h
%{_includedir}/qt5/Qt/qpictureformatplugin.h
%{_includedir}/qt5/Qt/qpixmap.h
%{_includedir}/qt5/Qt/qpixmapcache.h
%{_includedir}/qt5/Qt/qabstractpagesetupdialog.h
%{_includedir}/qt5/Qt/qabstractprintdialog.h
%{_includedir}/qt5/Qt/qcolordialog.h
%{_includedir}/qt5/Qt/qdialog.h
%{_includedir}/qt5/Qt/qerrormessage.h
%{_includedir}/qt5/Qt/qfiledialog.h
%{_includedir}/qt5/Qt/qfilesystemmodel.h
%{_includedir}/qt5/Qt/qfontdialog.h
%{_includedir}/qt5/Qt/qinputdialog.h
%{_includedir}/qt5/Qt/qmessagebox.h
%{_includedir}/qt5/Qt/qpagesetupdialog.h
%{_includedir}/qt5/Qt/qprintdialog.h
%{_includedir}/qt5/Qt/qprintpreviewdialog.h
%{_includedir}/qt5/Qt/qprogressdialog.h
%{_includedir}/qt5/Qt/qwizard.h
%{_includedir}/qt5/Qt/qabstractitemdelegate.h
%{_includedir}/qt5/Qt/qabstractitemview.h
%{_includedir}/qt5/Qt/qabstractproxymodel.h
%{_includedir}/qt5/Qt/qcolumnview.h
%{_includedir}/qt5/Qt/qdatawidgetmapper.h
%{_includedir}/qt5/Qt/qdirmodel.h
%{_includedir}/qt5/Qt/qfileiconprovider.h
%{_includedir}/qt5/Qt/qheaderview.h
%{_includedir}/qt5/Qt/qidentityproxymodel.h
%{_includedir}/qt5/Qt/qitemdelegate.h
%{_includedir}/qt5/Qt/qitemeditorfactory.h
%{_includedir}/qt5/Qt/qitemselectionmodel.h
%{_includedir}/qt5/Qt/qlistview.h
%{_includedir}/qt5/Qt/qlistwidget.h
%{_includedir}/qt5/Qt/qproxymodel.h
%{_includedir}/qt5/Qt/qsortfilterproxymodel.h
%{_includedir}/qt5/Qt/qstandarditemmodel.h
%{_includedir}/qt5/Qt/qstringlistmodel.h
%{_includedir}/qt5/Qt/qstyleditemdelegate.h
%{_includedir}/qt5/Qt/qtableview.h
%{_includedir}/qt5/Qt/qtablewidget.h
%{_includedir}/qt5/Qt/qtreeview.h
%{_includedir}/qt5/Qt/qtreewidget.h
%{_includedir}/qt5/Qt/qtreewidgetitemiterator.h
%{_includedir}/qt5/Qt/qgraphicsanchorlayout.h
%{_includedir}/qt5/Qt/qgraphicsgridlayout.h
%{_includedir}/qt5/Qt/qgraphicsitem.h
%{_includedir}/qt5/Qt/qgraphicsitemanimation.h
%{_includedir}/qt5/Qt/qgraphicslayout.h
%{_includedir}/qt5/Qt/qgraphicslayoutitem.h
%{_includedir}/qt5/Qt/qgraphicslinearlayout.h
%{_includedir}/qt5/Qt/qgraphicsproxywidget.h
%{_includedir}/qt5/Qt/qgraphicsscene.h
%{_includedir}/qt5/Qt/qgraphicssceneevent.h
%{_includedir}/qt5/Qt/qgraphicstransform.h
%{_includedir}/qt5/Qt/qgraphicsview.h
%{_includedir}/qt5/Qt/qgraphicswidget.h
%{_includedir}/qt5/Qt/qaction.h
%{_includedir}/qt5/Qt/qactiongroup.h
%{_includedir}/qt5/Qt/qapplication.h
%{_includedir}/qt5/Qt/qboxlayout.h
%{_includedir}/qt5/Qt/qclipboard.h
%{_includedir}/qt5/Qt/qcursor.h
%{_includedir}/qt5/Qt/qdesktopwidget.h
%{_includedir}/qt5/Qt/qdrag.h
%{_includedir}/qt5/Qt/qevent.h
%{_includedir}/qt5/Qt/qformlayout.h
%{_includedir}/qt5/Qt/qgesture.h
%{_includedir}/qt5/Qt/qgesturerecognizer.h
%{_includedir}/qt5/Qt/qgridlayout.h
%{_includedir}/qt5/Qt/qkeysequence.h
%{_includedir}/qt5/Qt/qlayout.h
%{_includedir}/qt5/Qt/qlayoutitem.h
%{_includedir}/qt5/Qt/qmime.h
%{_includedir}/qt5/Qt/qpalette.h
%{_includedir}/qt5/Qt/qsessionmanager.h
%{_includedir}/qt5/Qt/qshortcut.h
%{_includedir}/qt5/Qt/qsizepolicy.h
%{_includedir}/qt5/Qt/qsound*.h
%{_includedir}/qt5/Qt/qstackedlayout.h
%{_includedir}/qt5/Qt/qtooltip.h
%{_includedir}/qt5/Qt/qwhatsthis.h
%{_includedir}/qt5/Qt/qwidget.h
%{_includedir}/qt5/Qt/qwidgetaction.h
%{_includedir}/qt5/Qt/qbrush.h
%{_includedir}/qt5/Qt/qcolor.h
%{_includedir}/qt5/Qt/qcolormap.h
%{_includedir}/qt5/Qt/qdrawutil.h
%{_includedir}/qt5/Qt/qmatrix.h
%{_includedir}/qt5/Qt/qpaintdevice.h
%{_includedir}/qt5/Qt/qpaintengine.h
%{_includedir}/qt5/Qt/qpainter.h
%{_includedir}/qt5/Qt/qpainterpath.h
%{_includedir}/qt5/Qt/qpen.h
%{_includedir}/qt5/Qt/qpolygon.h
%{_includedir}/qt5/Qt/qprintengine.h
%{_includedir}/qt5/Qt/qprinter.h
%{_includedir}/qt5/Qt/qprinterinfo.h
%{_includedir}/qt5/Qt/qregion.h
%{_includedir}/qt5/Qt/qrgb.h
%{_includedir}/qt5/Qt/qstylepainter.h
%{_includedir}/qt5/Qt/qtransform.h
%{_includedir}/qt5/Qt/qwmatrix.h
%{_includedir}/qt5/Qt/qcdestyle.h
%{_includedir}/qt5/Qt/qcleanlooksstyle.h
%{_includedir}/qt5/Qt/qcommonstyle.h
%{_includedir}/qt5/Qt/qgtkstyle.h
%{_includedir}/qt5/Qt/qmotifstyle.h
%{_includedir}/qt5/Qt/qplastiquestyle.h
%{_includedir}/qt5/Qt/qproxystyle.h
%{_includedir}/qt5/Qt/qs60style.h
%{_includedir}/qt5/Qt/qstyle.h
%{_includedir}/qt5/Qt/qstylefactory.h
%{_includedir}/qt5/Qt/qstyleoption.h
%{_includedir}/qt5/Qt/qstyleplugin.h
%{_includedir}/qt5/Qt/qwindow*.h
%{_includedir}/qt5/Qt/qaccessible.h
%{_includedir}/qt5/Qt/qaccessible2.h
%{_includedir}/qt5/Qt/qaccessiblebridge.h
%{_includedir}/qt5/Qt/qaccessibleobject.h
%{_includedir}/qt5/Qt/qaccessibleplugin.h
%{_includedir}/qt5/Qt/qaccessiblewidget.h
%{_includedir}/qt5/Qt/qkeyeventtransition.h
%{_includedir}/qt5/Qt/qmouseeventtransition.h
%{_includedir}/qt5/Qt/qcopchannel_qws.h
%{_includedir}/qt5/Qt/qtransport*.h
%{_includedir}/qt5/Qt/qplatform*.h
%{_includedir}/qt5/Qt/qdecoration*.h
%{_includedir}/qt5/Qt/qdirectpainter_qws.h
%{_includedir}/qt5/Qt/qgenericplugin*.h
%{_includedir}/qt5/Qt/qguifunctions_*.h
%{_includedir}/qt5/Qt/qkbd*.h
%{_includedir}/qt5/Qt/qmaccocoa*
%{_includedir}/qt5/Qt/qmac*_mac.h
%{_includedir}/qt5/Qt/qmouse*.h
%{_includedir}/qt5/Qt/qscreen*.h
%{_includedir}/qt5/Qt/qx11*.h
%{_libdir}/fonts/
%{_libdir}/libQtGui.prl
%{_libdir}/libQtGui.so
%{_libdir}/pkgconfig/QtGui.pc
%{_datadir}/qt5/mkspecs/modules/qt_gui.pri


%files qtnetwork
%defattr(-,root,root,-)
%{_libdir}/libQtNetwork.so.5
%{_libdir}/libQtNetwork.so.5.*


%files qtnetwork-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/QtNetwork
%{_includedir}/qt5/QtNetwork/
%{_includedir}/qt5/Qt/qtnetworkversion.h
%{_includedir}/qt5/Qt/qabstractsocket.h
%{_includedir}/qt5/Qt/qlocalserver.h
%{_includedir}/qt5/Qt/qlocalsocket.h
%{_includedir}/qt5/Qt/qtcpserver.h
%{_includedir}/qt5/Qt/qtcpsocket.h
%{_includedir}/qt5/Qt/qudpsocket.h
%{_includedir}/qt5/Qt/qssl.h
%{_includedir}/qt5/Qt/qsslcertificate.h
%{_includedir}/qt5/Qt/qsslcipher.h
%{_includedir}/qt5/Qt/qsslconfiguration.h
%{_includedir}/qt5/Qt/qsslerror.h
%{_includedir}/qt5/Qt/qsslkey.h
%{_includedir}/qt5/Qt/qsslsocket.h
%{_includedir}/qt5/Qt/qnetworkconfigmanager.h
%{_includedir}/qt5/Qt/qnetworkconfiguration.h
%{_includedir}/qt5/Qt/qnetworksession.h
%{_includedir}/qt5/Qt/qauthenticator.h
%{_includedir}/qt5/Qt/qhostaddress.h
%{_includedir}/qt5/Qt/qhostinfo.h
%{_includedir}/qt5/Qt/qnetworkinterface.h
%{_includedir}/qt5/Qt/qnetworkproxy.h
%{_includedir}/qt5/Qt/qurlinfo.h
%{_includedir}/qt5/Qt/qabstractnetworkcache.h
%{_includedir}/qt5/Qt/qftp.h
%{_includedir}/qt5/Qt/qhttp.h
%{_includedir}/qt5/Qt/qhttpmultipart.h
%{_includedir}/qt5/Qt/qnetworkaccessmanager.h
%{_includedir}/qt5/Qt/qnetworkcookie.h
%{_includedir}/qt5/Qt/qnetworkcookiejar.h
%{_includedir}/qt5/Qt/qnetworkdiskcache.h
%{_includedir}/qt5/Qt/qnetworkreply.h
%{_includedir}/qt5/Qt/qnetworkrequest.h
%{_libdir}/libQtNetwork.prl
%{_libdir}/libQtNetwork.so
%{_libdir}/pkgconfig/QtNetwork.pc
%{_datadir}/qt5/mkspecs/modules/qt_network.pri


%files qtopengl
%defattr(-,root,root,-)
%{_libdir}/libQtOpenGL.so.5
%{_libdir}/libQtOpenGL.so.5.*


%files qtopengl-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/QtOpenGL
%{_includedir}/qt5/QtOpenGL/
%{_includedir}/qt5/Qt/qgl.h
%{_includedir}/qt5/Qt/qglbuffer.h
%{_includedir}/qt5/Qt/qglcolormap.h
%{_includedir}/qt5/Qt/qglframebufferobject.h
%{_includedir}/qt5/Qt/qglfunctions.h
%{_includedir}/qt5/Qt/qglpixelbuffer.h
%{_includedir}/qt5/Qt/qglshaderprogram.h
%{_includedir}/qt5/Qt/qtopenglversion.h
%{_includedir}/qt5/Qt/qglscreen_qws.h
%{_libdir}/libQtOpenGL.prl
%{_libdir}/libQtOpenGL.so
%{_libdir}/pkgconfig/QtOpenGL.pc
%{_datadir}/qt5/mkspecs/modules/qt_opengl.pri


%files qtsql
%defattr(-,root,root,-)
%{_libdir}/libQtSql.so.5
%{_libdir}/libQtSql.so.5.*


%files qtsql-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/QtSql
%{_includedir}/qt5/QtSql/
%{_includedir}/qt5/Qt/qtsqlversion.h
%{_includedir}/qt5/Qt/qsqlquerymodel.h
%{_includedir}/qt5/Qt/qsqlrelationaldelegate.h
%{_includedir}/qt5/Qt/qsqlrelationaltablemodel.h
%{_includedir}/qt5/Qt/qsqltablemodel.h
%{_includedir}/qt5/Qt/qsql.h
%{_includedir}/qt5/Qt/qsqldatabase.h
%{_includedir}/qt5/Qt/qsqldriver.h
%{_includedir}/qt5/Qt/qsqldriverplugin.h
%{_includedir}/qt5/Qt/qsqlerror.h
%{_includedir}/qt5/Qt/qsqlfield.h
%{_includedir}/qt5/Qt/qsqlindex.h
%{_includedir}/qt5/Qt/qsqlquery.h
%{_includedir}/qt5/Qt/qsqlrecord.h
%{_includedir}/qt5/Qt/qsqlresult.h
%{_includedir}/qt5/Qt/qsql_*.h
%{_libdir}/libQtSql.prl
%{_libdir}/libQtSql.so
%{_libdir}/pkgconfig/QtSql.pc
%{_datadir}/qt5/mkspecs/modules/qt_sql.pri


%files qttest
%defattr(-,root,root,-)
%{_libdir}/libQtTest.so.5
%{_libdir}/libQtTest.so.5.*

%files qttest-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/QtTest
%{_includedir}/qt5/QtTest/
%{_includedir}/qt5/Qt/qttestversion.h
%{_includedir}/qt5/Qt/qbenchmark.h
%{_includedir}/qt5/Qt/qbenchmarkmetric.h
%{_includedir}/qt5/Qt/qsignalspy.h
%{_includedir}/qt5/Qt/qtest*.h
%{_libdir}/libQtTest.prl
%{_libdir}/libQtTest.so
%{_libdir}/pkgconfig/QtTest.pc
%{_datadir}/qt5/mkspecs/modules/qt_testlib.pri

%files qtxml
%defattr(-,root,root,-)
%{_libdir}/libQtXml.so.5
%{_libdir}/libQtXml.so.5.*

%files qtxml-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/Qt/QtXml
%{_includedir}/qt5/QtXml/
%{_includedir}/qt5/Qt/qtxmlversion.h
%{_includedir}/qt5/Qt/qxmlstream.h
%{_includedir}/qt5/Qt/qxml.h
%{_includedir}/qt5/Qt/qdom.h
%{_libdir}/libQtXml.prl
%{_libdir}/libQtXml.so
%{_libdir}/pkgconfig/QtXml.pc
%{_datadir}/qt5/mkspecs/modules/qt_xml.pri

#%files qtuitools
#%defattr(-,root,root,-)
#%{_libdir}/libQtUiTools.so.5
#%{_libdir}/libQtUiTools.so.5.*

%files qtuitools-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtUiTools/
%{_libdir}/libQtUiTools.prl
#%{_libdir}/libQtUiTools.so
%{_libdir}/pkgconfig/QtUiTools.pc
%{_datadir}/qt5/mkspecs/modules/qt_uitools.pri

%files qtdesigner-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtDesigner/
%{_datadir}/qt5/mkspecs/modules/qt_uilib.pri



# Plugin packages

%files plugin-accessible-libqtaccessiblewidgets
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/accessible/libqtaccessiblewidgets.so

%files plugin-bearer-connman
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/bearer/libqconnmanbearer.so

%files plugin-bearer-generic
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/bearer/libqgenericbearer.so

%files plugin-bearer-nm
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/bearer/libqnmbearer.so

%files plugin-imageformat-gif
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqgif.so

%files plugin-imageformat-ico
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqico.so

%files plugin-imageformat-jpeg
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqjpeg.so

%files plugin-imageformat-mng
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqmng.so

%files plugin-imageformat-tiff
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqtiff.so

%files plugin-platform-minimal
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqminimal.so

%files plugin-platform-wayland
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqwayland.so

%files plugin-platform-eglfs
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqeglfs.so

%files plugin-sqldriver-sqlite
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/sqldrivers/libqsqlite.so

%files plugin-inputmethod-imsw-multi
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/inputmethods/libqimsw-multi.so




#### Changelog section

%changelog
* Thu Jun 30 2011 Mika Boström <mika.bostrom@nomovok.com> - 4.9.90.20110630
- Add more packages to further split the build into reasonable
  components. Use the includes in qt5/Qt/Qt* files as guide.
* Wed Jun 29 2011 Mika Boström <mika.bostrom@nomovok.com> - 4.9.90.20110627
- Start working on completely modular build, splitting everything in new
  Qt5 tree to smaller components.
- Removed "-demosdir" from configure line entirely. It is no longer
  available.

