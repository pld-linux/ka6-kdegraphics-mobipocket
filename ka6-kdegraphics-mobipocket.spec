%define		kf_ver		5.94.0
%define		qt_ver		6.4.0
%define		kaname		kdegraphics-mobipocket
Summary:	KDE graphics mobipocket library
Summary(pl.UTF-8):	Biblioteka KDE graphics mobipocket
Name:		ka6-%{kaname}
Version:	25.04.2
Release:	2
License:	GPL v2+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{version}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	ba527148ce6ae8bf174cde1adb731973
URL:		https://kde.org/
BuildRequires:	Qt6Core-devel >= %{qt_ver}
BuildRequires:	Qt6Gui-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-tools
BuildRequires:	kf6-extra-cmake-modules >= %{kf_ver}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt6Core >= %{qt_ver}
Requires:	Qt6Gui >= %{qt_ver}
# don't obsolete until ka5 exists on ftp
#Obsoletes:	ka5-kdegraphics-mobipocket < 24
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to support mobipocket ebooks.

%description -l pl.UTF-8
Biblioteka do obsługi e-booków mobipocket.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt6Core-devel >= %{qt_ver}
Requires:	Qt6Gui-devel >= %{qt_ver}
#Obsoletes:	ka5-kdegraphics-mobipocket-devel < 24

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQMobipocket6.so.*.*
%ghost %{_libdir}/libQMobipocket6.so.2

%files devel
%defattr(644,root,root,755)
%{_libdir}/libQMobipocket6.so
%{_includedir}/QMobipocket6
%{_libdir}/cmake/QMobipocket6
