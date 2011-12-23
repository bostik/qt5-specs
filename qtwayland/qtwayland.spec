%define _qtmodule_snapshot_version %nil
Name:       qt5-qtwayland
Summary:    Qt Wayland compositor
Version:    %{_qtmodule_snapshot_version}
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.gz
Patch10:    wayland-wrapper-includes.patch
Patch11:    install-base-from-environ.patch
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qtopengl-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  libX11-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libffi-devel
BuildRequires:  fdupes

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt wayland compositor


%package devel
Summary:        Qt Wayland compositor - development files
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt wayland compositor development files


#### Build section

%prep
%setup -q -n %{name}
%patch10 -p1
%patch11 -p1


%build
export QTDIR=/usr/share/qt5
export INSTALLBASE=/usr
qmake
make %{?_smp_flags}

%install
rm -rf %{buildroot}
%qmake_install
# Fix wrong path in pkgconfig files
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
-exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;
%fdupes %{buildroot}/%{_includedir}


#### Pre/Post section

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


#### File section

%files
%defattr(-,root,root,-)
%{_libdir}/libqt-compositor.so.*


%files devel
%defattr(-,root,root,-)
%{_includedir}/qt-compositor/
%{_libdir}/libqt-compositor.so



#### No changelog section, separate $pkg.changes contains the history

