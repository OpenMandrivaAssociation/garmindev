%define	major 0
%define libname	%mklibname garmindev %{major}
%define develname %mklibname -d garmindev

Summary:	Drivers for communication with Garmin GPS devices
Name:		garmindev
Version:	0.3.4
Release:	2
Group:		System/Libraries
License:	GPLv2+
URL:		http://www.qlandkarte.org
Source0:	http://downloads.sourceforge.net/qlandkartegt/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	pkgconfig(libusb)

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
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
%cmake ..
%make VERBOSE=1

%install
rm -rf %{buildroot}
cd build
%makeinstall_std

# fix perms on plugins
find %{buildroot}%{_libdir}/qlandkartegt -type f -exec chmod 0755 {} \;

# drop the development files
rm -rf %{buildroot}%{_includedir}/garmin
rm -rf %{buildroot}%{_libdir}/qlandkartegt/libgarmin*

%files -n %{libname}
%{_libdir}/qlandkartegt


