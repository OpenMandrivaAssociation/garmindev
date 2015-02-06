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



%changelog
* Wed Sep 22 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-1mdv2011.0
+ Revision: 580538
- import garmindev


* Wed Sep 22 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-1mdv2010.1
- initial Mandriva package (fedora import)

* Sun Jul  4 2010 Dan Horák <dan[at]danny.cz> 0.3.4-1
- update to version 0.3.4

* Sun Feb  6 2010 Dan Horák <dan[at]danny.cz> 0.3.3-1
- update to version 0.3.3

* Tue Jan 26 2010 Dan Horák <dan[at]danny.cz> 0.3.2-1
- update to version 0.3.2

* Wed Dec 23 2009 Dan Horák <dan[at]danny.cz> 0.3.1-1
- update to version 0.3.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Dan Horák <dan[at]danny.cz> 0.3.0-1
- update to version 0.3.0

* Wed Apr 15 2009 Dan Horák <dan[at]danny.cz> 0.1.1-1
- update to version 0.1.1

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.20090208svn1152
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  8 2009 Dan Horák <dan[at]danny.cz> 0-0.3.20090208svn1152
- update to revision 1152 - adds support for eTrex LegendHCx, eTrexH, eTrex Legend

* Wed Nov 19 2008 Dan Horák <dan[at]danny.cz> 0-0.2.20081117svn928
- provide garmindev(interface) = 1.15 for correct interraction with QLandkarteGT

* Mon Nov 17 2008 Dan Horák <dan[at]danny.cz> 0-0.1.20081117svn928
- initial Fedora version
