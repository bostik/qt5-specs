%define _qtmodule_snapshot_version %nil
Name:       qt5-qtxmlpatterns
Summary:    Qt XML Patterns library
Version:    %{_qtmodule_snapshot_version}
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.gz
Patch0:     disable-xmlpattern-examples-install.patch
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtxml-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qmake
BuildRequires:  fdupes

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the XMLPatterns library


%package devel
Summary:    Qt XML Patterns - development files
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the XMLPatterns library development files


#### Build section

%prep
%setup -q -n %{name}
%patch0 -p1


# The original source assumes build happens within a monolithic tree.
# The tool used is syncqt, which complains a lot but really only wants
# to know where the mkspecs may be found. Hence the environment variable
# name is a little misleading.
#
# XXX: FOR THE LOVE OF ALL THAT MAY BE HOLY - DO NOT USE RPMBUILD AND
# ITS INTERNAL qmake MACRO. IT BREAKS THE BUILD!
%build
export QTDIR=/usr/share/qt5
qmake
make %{?_smp_flags}

%install
rm -rf %{buildroot}
%qmake_install
%fdupes %{buildroot}/%{_includedir}




#### Pre/Post section

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig




#### File section


%files
%defattr(-,root,root,-)
%{_libdir}/libQtXmlPatterns.so.5
%{_libdir}/libQtXmlPatterns.so.5.*
%{_bindir}/*

# FIXME: the provided .pc file is empty!
# Find out what gives and find a clean resolution
%files devel
%defattr(-,root,root,-)
%{_libdir}/libQtXmlPatterns.so
%{_libdir}/libQtXmlPatterns.la
%{_libdir}/pkgconfig/*
%{_includedir}/qt5/
%{_datadir}/qt5/mkspecs/


#### No changelog section, separate $pkg.changes contains the history
