%define _qtmodules_snapshot_version %nil
Name:       qt5-qttools
Summary:    Development tools for Qt
Version:    %{_qtmodules_snapshot_version}
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source:     %{name}-%{version}.tar.gz
Patch0:     add_qtclucene_dir.patch
Patch1:     add_qthelp_search_path.patch
Patch2:     link_qcollectiongenerator_with_qthelp.patch
Patch3:     link_qhelpconverter_with_qthelp.patch
Patch4:     link_qhelpgenerator_with_qthelp.patch
Patch5:     fix_qtdesigner_include_paths.patch
Patch6:     copy_widgets_table_from_base.patch
Patch7:     embed_rcc.patch
Patch8:     fix_libqtdesigner_destdir.patch
Patch8:     fix_libqtdesignercomponents_destdir.patch
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtsql-devel
BuildRequires:  qt5-qtxml-devel
BuildRequires:  qt5-qtdesigner-devel
BuildRequires:  qt5-qmake
BuildRequires:  qt5-tools
BuildRequires:  fdupes
#Requires:       qt5-qmake = %{version}

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains additional tools for building Qt applications.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
export QTDIR=/usr/share/qt5
qmake
make %{?_smp_flags}

%install
rm -rf %{buildroot}
%qmake_install


#### Pre/Post section

%post
/sbin/ldconfig
%postun
/sbin/ldconfig



%files
%defattr(-,root,root,-)
%{_bindir}/*



#### No changelog section, separate $pkg.changes contains the history

