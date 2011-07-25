%define _qtmodule_snapshot_version %nil
Name:       qt5-qtmultimediakit
Summary:    Qt MultimediaKit module
Version:    %{_qtmodule_snapshot_version}
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.gz
Patch0:     disable_examples_install.patch
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qtxmlpatterns-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtopengl-devel
BuildRequires:  qt5-qtdeclarative-qtquick1-devel
BuildRequires:  qt5-qmake
BuildRequires:  pkgconfig(alsa)
BuildRequires:  fdupes

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the QtMultimediaKit module


%package devel
Summary:    Qt MultimediaKit - development files
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the QtMultimediaKit module development files

%package -n qt5-qtdeclarative-import-multimedia
Summary:    QtDeclarative multimedia import
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}
Requires:   qt5-declarative

%description -n qt5-qtdeclarative-import-multimedia
This package contains the Multimedia import for QtDeclarative

%package plugin-mediaservice-audioengine
Summary:    Qt MultimediaKit - audio engine media-service
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-mediaservice-audioengine
This package contains the audio engine plugin for media-service

%package plugin-mediaservice-v4lengine
Summary:    Qt MultimediaKit - V4L engine for media-service
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-mediaservice-v4lengine
This package contains the V4L engine plugin for media-service

%package plugin-playlistformats-m3u
Summary:    Qt MultimediaKit - M3U playlist support
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description plugin-playlistformats-m3u
This package contains the M3U playlist support





#### Build section

%prep
%setup -q -n %{name}
%patch0 -p1


%build
export QTDIR=/usr/share/qt5
qmake
make %{?_smp_flags}

%install
rm -rf %{buildroot}
%make_install
%fdupes %{buildroot}/%{_includedir}




#### Pre/Post section

%post
/sbin/ldconfig
%postun
/sbin/ldconfig




#### File section


%files
%defattr(-,root,root,-)
%{_libdir}/libQtMultimediaKit.so.5
%{_libdir}/libQtMultimediaKit.so.5.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libQtMultimediaKit.so
%{_libdir}/pkgconfig/*
%{_includedir}/qt5/*
%{_datadir}/qt5/mkspecs/

%files -n qt5-qtdeclarative-import-multimedia
%defattr(-,root,root,-)
%{_libdir}/qt5/imports/Qt/multimediakit/

%files plugin-mediaservice-audioengine
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/mediaservice/libqtmedia_audioengine.so

%files plugin-mediaservice-v4lengine
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/mediaservice/libqtmedia_v4lengine.so

%files plugin-playlistformats-m3u
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/playlistformats/libqtmultimediakit_m3u.so


#### No changelog section, separate $pkg.changes contains the history
