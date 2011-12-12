%define _qtmodule_snapshot_version %nil
Name:       qt5-qtquick3d
Summary:    Qt Quick #d
Version:    %{_qtmodule_snapshot_version}
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.gz
Patch1:     0001-Update-to-match-class-renames.patch
Patch2:     0002-Add-a-pri-file-to-include-threed-header-paths.patch
Patch3:     0003-Add-build-fixes-to-QtQuick3D-imports.patch
Patch4:     0004-Fix-quick3d-include-path.patch
Patch5:     0005-Use-load-operator-for-atomic-int.patch
Patch6:     0006-Add-missing-QWindow-include.patch
Patch7:     0007-Use-QQuick-item-names.patch
Patch8:     0008-Use-header-includes-for-bezier-plugin.patch
Patch9:     0009-Use-header-includes-for-assimp-plugin.patch
Patch10:    0010-Use-header-includes-for-tga-plugin.patch
Patch11:    0011-Remove-extra-stuff-from-build.patch
Patch12:    0012-Install-public-headers.patch
Patch13:    0013-Install-QtQuick3D-public-headers.patch
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qtopengl-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtdeclarative-qtquick-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  fdupes

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt Quick 3D library


%package devel
Summary:        Qt Quick 3D - development files
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt Quick 3D development files


%package plugin-imageformat-tga
Summary:        Qt Quick 3D - TGA image format plugin
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description plugin-imageformat-tga
This package contains the TGA image format plugin

%package plugin-sceneformat-ai
Summary:        Qt Quick 3D - all-inclusive scene format plugin
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description plugin-sceneformat-ai
This package contains the all-inclusive scene format plugin

%package plugin-sceneformat-bezier
Summary:        Qt Quick 3D - bezier scene format plugin
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description plugin-sceneformat-bezier
This package contains the bezier scene format plugin


%package -n qt5-qtdeclarative-import-qt3d-shapes
Summary:        Qt Quick 3D - declarative Qt3D shapes import
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description -n qt5-qtdeclarative-import-qt3d-shapes
This package contains the Qt3D shapes import for QtDeclarative

%package -n qt5-qtdeclarative-import-qt3d
Summary:        Qt Quick 3D - declarative Qt3D import
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description -n qt5-qtdeclarative-import-qt3d
This package contains the Qt3D import for QtDeclarative


#### Build section

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
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1


%build
export QTDIR=/usr/share/qt5
%qmake CONFIG+=package
make %{?_smp_flags}

%install
rm -rf %{buildroot}
%qmake_install
# Remove unneeded .la files
rm -f %{buildroot}/%{_libdir}/*.la
%fdupes %{buildroot}/%{_includedir}


#### Pre/Post section

%post
/sbin/ldconfig
%postun
/sbin/ldconfig

#### File section

%files
%defattr(-,root,root,-)
%{_libdir}/libQt3D.so.5
%{_libdir}/libQt3D.so.5.*
%{_libdir}/libQt3DQuick.so.5
%{_libdir}/libQt3DQuick.so.5.*


%files devel
%defattr(-,root,root,-)
%{_libdir}/libQt3D.so
%{_libdir}/libQt3DQuick.so
%{_includedir}/qt5/Qt3D/
%{_libdir}/pkgconfig/
%{_datadir}/qt5/mkspecs/


%files plugin-imageformat-tga
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqtga.so

%files plugin-sceneformat-ai
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/sceneformats/libqsceneai.so

%files plugin-sceneformat-bezier
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/sceneformats/libqscenebezier.so

%files -n qt5-qtdeclarative-import-qt3d-shapes
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/Qt3D/Shapes/

%files -n qt5-qtdeclarative-import-qt3d
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/Qt3D/libqthreedqmlplugin.so

#### No changelog section, separate $pkg.changes contains the history

