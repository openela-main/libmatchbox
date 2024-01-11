Summary:        Libraries for the Matchbox Desktop
Name:           libmatchbox 
Version:        1.9
Release:        23%{?dist}
Url:            http://projects.o-hand.com/matchbox/
License:        LGPLv2+
Group:          Development/Libraries 
Source:         http://projects.o-hand.com/matchbox/sources/libmatchbox/%{version}/%{name}-%{version}.tar.bz2
Patch0:         libmatchbox-1.9-add-needed.patch
Patch1:		libmatchbox-1.9-libpng.patch
BuildRequires:  pango-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  check-devel
BuildRequires:  autoconf automake libtool
Buildroot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

%package devel
Group:          Development/C
Summary:        Static libraries and header files from %{name}
Provides:       matchbox-devel = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}-%{release}
Provides:       libmb-devel = %{version}-%{release}
Requires:       libmatchbox = %{version}
Requires:       pkgconfig

%description devel
Static libraries and header files from %{name}

%prep
%setup -q
%patch0 -p1 -b .add-needed
%patch1 -p1 -b .libpng

%build
autoreconf -v --install
%configure --enable-png --enable-jpeg --enable-pango
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files 
%_libdir/*.so.*

%files devel
%doc AUTHORS ChangeLog README COPYING
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%dir %{_includedir}/libmb
%{_includedir}/libmb/*.h

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.9-12
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.9-11
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 17 2011 Adam Jackson <ajax@redhat.com> 1.9-8
- libmatchbox-1.9-libpng.patch: libpng 1.5 compatibility

* Tue Feb 16 2010 Adam Jackson <ajax@redhat.com> 1.9-7
- libmatchbox-1.9-add-needed.patch: Fix FTBFS from --no-add-needed

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Aug  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.9-4
- fix license tag

* Tue Jun 19 2007 John (J5) Palmieri <johnp@redhat.com> 1.9-3
- Fixed License to be LGPL
- Add COPYING license file to docs
- Fixed Group
- Fixed buildroot
- Added {} braces around % macros
- Removed .la and .a files 
- Own {_includedir}/libmb directory
- Add dist tag to release
- Add smpflags  flag to make
- Remove use of boken makeinstall macro
 
* Mon Aug 21 2006 Marco Pesenti Gritti <mpg@redhat.com> 1.9-2
- Disable xsettings

* Mon Aug 21 2006 Marco Pesenti Gritti <mpg@redhat.com> 1.9-1
- Update to 1.9

* Thu May 12 2005 Austin Acton <austin@mandriva.org> 1.7-1mdk
- New release 1.7
- fix URLs

* Mon Jan 24 2005 Austin Acton <austin@mandrake.org> 1.6-1mdk
- 1.6

* Tue Jan 4 2005 Austin Acton <austin@mandrake.org> 1.5-1mdk
- 1.5

* Wed Sep 29 2004 Austin Acton <austin@mandrake.org> 1.4-1mdk
- 1.4

* Mon Aug 23 2004 Austin Acton <austin@mandrake.org> 1.3-1mdk
- 1.3

* Mon Jul 20 2004 Austin Acton <austin@mandrake.org> 1.2-1mdk
- initial package
