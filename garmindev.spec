%define	major 0
%define libname	%mklibname garmindev %{major}
%define develname %mklibname -d garmindev

Summary:	Drivers for communication with Garmin GPS devices
Name:		garmindev
Version:	0.3.4
Release:	%mkrel 1
Group:		System/Libraries
License:	GPLv2+
URL:		http://www.qlandkarte.org
Source0:	http://downloads.sourceforge.net/qlandkartegt/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	libusb-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
Drivers for communication with Garmin GPS devices used by QLandkarteGT.

%package -n	%{libname}
Summary:	Drivers for communication with Garmin GPS devices
Group:          System/Libraries
Provides:	%{name}(interface) = 1.18
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
Drivers for communication with Garmin GPS devices used by QLandkarteGT.

%prep
%setup -q

%build
%cmake
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

# fix perms on plugins
find %{buildroot}%{_libdir}/qlandkartegt -type f -exec chmod 0755 {} \;

# drop the development files
rm -rf %{buildroot}%{_includedir}/garmin
rm -rf %{buildroot}%{_libdir}/qlandkartegt/libgarmin*

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/qlandkartegt

