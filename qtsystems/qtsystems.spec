Name:       qt5-systems
Summary:    Qt System modules
Version:    4.9.90.20110701+g4759327
Release:    1%{?dist}
Group:      System/Libraries
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}.tar.gz
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qtsql-devel
BuildRequires:  qt5-qtdbus-devel
BuildRequires:  qt5-qtxml-devel
BuildRequires:  qt5-declarative-devel
BuildRequires:  qt5-qmake
BuildRequires:  fontconfig-devel
BuildRequires:  fdupes

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt system modules


%package -n qt5-systeminfo
Summary:    Qt system info
Group:      System/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-systeminfo
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt SystemInfo module


%package -n qt5-systeminfo-devel
Summary:    Qt system info - development files
Group:      Development/Libraries
Requires:   qt5-systeminfo

%description -n qt5-systeminfo-devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt SystemInfo development files


%package -n qt5-declarative-systeminfo
Summary:    Qt system info import for QtDeclarative
Group:      System/Libraries
Requires:   qt5-declarative

%description -n qt5-declarative-systeminfo
This package contains the system info import for QtDeclarative


%package -n qt5-serviceframework
Summary:    Qt Service Framework
Group:      System/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-serviceframework
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt Service Framework module

%package -n qt5-serviceframework-devel
Summary:    Qt Service Framework - development files
Group:      Development/Libraries
Requires:   qt5-serviceframework

%description -n qt5-serviceframework-devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt Service Framework development files


%package -n qt5-declarative-serviceframework
Summary:    Qt Service Framework import for QtDeclarative
Group:      System/Libraries
Requires:   qt5-declarative

%description -n qt5-declarative-serviceframework
This package contains the Service Framework import for QtDeclarative



%package -n qt5-publishsubscribe
Summary:    Qt PublishSubscribe module
Group:      System/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-publishsubscribe
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt PublishSubscribe module

%package -n qt5-publishsubscribe-devel
Summary:    Qt PublishSubscribe - development files
Group:      Development/Libraries
Requires:   qt5-publishsubscribe

%description -n qt5-publishsubscribe-devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt PublishSubscribe development files


%package -n qt5-declarative-publishsubscribe
Summary:    Qt PublishSubscribe import for QtDeclarative
Group:      System/Libraries
Requires:   qt5-declarative

%description -n qt5-declarative-publishsubscribe
This package contains the PublishSuvbscribe import for QtDeclarative




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
%fdupes %{buildroot}/%{_includedir}




#### Pre/Post section

%post -n qt5-systeminfo
/sbin/ldconfig
%postun -n qt5-systeminfo
/sbin/ldconfig

%post -n qt5-serviceframework
/sbin/ldconfig
%postun -n qt5-serviceframework
/sbin/ldconfig

%post -n qt5-publishsubscribe
/sbin/ldconfig
%postun -n qt5-publishsubscribe
/sbin/ldconfig



#### File section


%files -n qt5-systeminfo
%defattr(-,root,root,-)
%{_libdir}/libQtSystemInfo.so.5
%{_libdir}/libQtSystemInfo.so.5.*

%files -n qt5-systeminfo-devel
%defattr(-,root,root,-)
%{_libdir}/libQtSystemInfo.so
%{_libdir}/pkgconfig/QtSystemInfo.pc
%{_includedir}/qt5/Qt/QtSystemInfo
%{_includedir}/qt5/Qt/qtsysteminfoversion.h
%{_includedir}/qt5/Qt/q*info.h
%{_includedir}/qt5/Qt/qdeviceprofile.h
%{_includedir}/qt5/Qt/qscreensaver.h
%{_includedir}/qt5/QtSystemInfo/
%{_datadir}/qt5/mkspecs/modules/qt_systeminfo.pri

%files -n qt5-declarative-systeminfo
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/Qt/systeminfo/

%files -n qt5-serviceframework
%defattr(-,root,root,-)
%{_bindir}/servicefw
%{_libdir}/libQtServiceFramework.so.5
%{_libdir}/libQtServiceFramework.so.5.*

%files -n qt5-serviceframework-devel
%defattr(-,root,root,-)
%{_libdir}/libQtServiceFramework.so
%{_libdir}/pkgconfig/QtServiceFramework.pc
%{_includedir}/qt5/Qt/QtServiceFramework
%{_includedir}/qt5/Qt/qtserviceframeworkversion.h
%{_includedir}/qt5/Qt/qabstractsecuritysession.h
%{_includedir}/qt5/Qt/qremoteservice*.h
%{_includedir}/qt5/Qt/qservice*.h
%{_includedir}/qt5/QtServiceFramework/
%{_datadir}/qt5/mkspecs/modules/qt_serviceframework.pri

%files -n qt5-declarative-serviceframework
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/Qt/serviceframework/




%files -n qt5-publishsubscribe
%defattr(-,root,root,-)
%{_libdir}/libQtPublishSubscribe.so.5
%{_libdir}/libQtPublishSubscribe.so.5.*

%files -n qt5-publishsubscribe-devel
%defattr(-,root,root,-)
%{_libdir}/libQtPublishSubscribe.so
%{_libdir}/pkgconfig/QtPublishSubscribe.pc
%{_includedir}/qt5/Qt/QtPublishSubscribe
%{_includedir}/qt5/Qt/qtpublishsubscribeversion*.h
%{_includedir}/qt5/Qt/qvalue*.h
%{_includedir}/qt5/QtPublishSubscribe/
%{_datadir}/qt5/mkspecs/modules/qt_publishsubscribe.pri

%files -n qt5-declarative-publishsubscribe
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/Qt/publishsubscribe/


#### Changelog section

%changelog
* Fri Jul  8 2011 Mika Boström <mika.bostrom@nomovok.com> - 4.9.90.20110701
- Initial packaging
- Builds against packages from qtbase build

