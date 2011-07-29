%define _qtmodule_snapshot_version %nil
Name:       qt5-qtsvg
Summary:    Qt scripting module
Version:    %{_qtmodule_snapshot_version}
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtxml-devel
BuildRequires:  qt5-qmake
BuildRequires:  fdupes

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the SVG module


%package devel
Summary:    Qt SVG - development files
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the SVG module development files

%package plugin-imageformat-svg
Summary:    Qt SVG image format plugin
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-imageformat-svg
This package contains the SVG image format plugin



#### Build section

%prep
%setup -q -n %{name}


%build
export QTDIR=/usr/share/qt5
qmake
make %{?_smp_flags}

%install
rm -rf %{buildroot}
%qmake_install
%fdupes %{buildroot}/%{_includedir}




#### Pre/Post section

%post
/sbin/ldconfig
%postun
/sbin/ldconfig




#### File section


%files
%defattr(-,root,root,-)
%{_libdir}/libQtSvg.so.5
%{_libdir}/libQtSvg.so.5.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libQtSvg.la
%{_libdir}/libQtSvg.so
%{_libdir}/pkgconfig/*
%{_includedir}/qt5/*
%{_datadir}/qt5/mkspecs/

%files plugin-imageformat-svg
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/lib*svg.so



#### No changelog section, separate $pkg.changes contains the history
