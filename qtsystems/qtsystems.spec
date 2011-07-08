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
Requires:   qt5-systeminfo = %{version}-%{release}

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



#### Changelog section

%changelog
* Fri Jul  8 2011 Mika Boström <mika.bostrom@nomovok.com> - 4.9.90.20110701
- Initial packaging
- Builds against packages from qtbase build

