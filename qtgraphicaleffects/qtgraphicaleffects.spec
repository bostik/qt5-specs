%define _qtmodule_snapshot_version %nil
Name:       qt5-qtgraphicaleffects
Summary:    Qt Graphical effects
Version:    %{_qtmodule_snapshot_version}
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt Graphical Effects

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

%files
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtGraphicalEffects/Blend.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/BrightnessContrast.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/ColorOverlay.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/Colorize.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/ConicalGradient.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/Desaturate.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/DirectionalBlur.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/Displace.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/DropShadow.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/FastBlur.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/GammaAdjust.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/GaussianBlur.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/Glow.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/HueSaturation.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/InnerShadow.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/LevelAdjust.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/LinearGradient.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/MaskedBlur.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/OpacityMask.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/RadialBlur.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/RadialGradient.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/RectangularGlow.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/RecursiveBlur.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/ThresholdMask.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/ZoomBlur.qml
%{_libdir}/qt5/qml/QtGraphicalEffects/private/*
%{_libdir}/qt5/qml/QtGraphicalEffects/qmldir

#### No changelog section, separate $pkg.changes contains the history
