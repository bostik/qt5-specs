%define _qtmodule_snapshot_version %nil
Name:       qt5-qtimageformats
Summary:    Qt Imageformats
Version:    %{_qtmodule_snapshot_version}
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.gz
Patch1:     destdir.patch
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt Image Formats plugin

#### Build section

%prep
%setup -q -n %{name}
%patch1 -p1

%build
export QTDIR=/usr/share/qt5
%qmake
make %{?_smp_flags}

%install
rm -rf %{buildroot}
%qmake_install

%files
%defattr(-,root,root,-)
%_libdir/qt5/plugins/imageformats/*.so

#### No changelog section, separate $pkg.changes contains the history