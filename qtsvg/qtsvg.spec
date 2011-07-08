Name:       qt5-svg
Summary:    Qt scripting module
Version:    4.9.90.20110701+gf9d233b7
Release:    1%{?dist}
Group:      System/Libraries
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}.tar.gz
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtxml-devel
BuildRequires:  qt5-qmake
BuildRequires:  fontconfig-devel

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the SVG module


%package devel
Summary:    Qt SVG - development files
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the SVG module development files


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




#### Pre/Post section

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig




#### File section


%files
%defattr(-,root,root,-)
%{_libdir}/libQtSvg.so.5
%{_libdir}/libQtSvg.so.5.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libQtSvg.so
%{_libdir}/pkgconfig/*
%{_includedir}/qt5/*
%{_datadir}/qt5/mkspecs/



#### Changelog section

%changelog
* Thu Jul  7 2011 Mika Boström <mika.bostrom@nomovok.com> - 4.9.90.20110701
- Initial packaging
- Builds against packages from qtbase build

