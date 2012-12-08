%define api_version	2
%define lib_major	0
%define lib_name	%mklibname IDL %{api_version} %{lib_major}
%define develname	%mklibname -d  IDL %{api_version}

Summary:	IDL parsing library
Name:		libIDL
Version:	0.8.14
Release:	8
URL:		http://orbit-resource.sf.net/
License:	LGPLv2+
Group:		System/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2

BuildConflicts:	ORBit-devel < 0.5.10
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	pkgconfig(glib-2.0)

%description
libIDL is a small library for creating parse trees of CORBA v2.2
compliant Interface Definition Language (IDL) files, which is a
specification for defining interfaces which can be used between
different CORBA implementations.

%package -n %{lib_name}
Summary:	%{summary}
Group:		%{group}
Provides:	%{name} = %{version}-%{release}
Provides:	%{name}%{api_version} = %{version}-%{release}

%description -n %{lib_name}
libIDL is a small library for creating parse trees of CORBA v2.2
compliant Interface Definition Language (IDL) files, which is a
specification for defining interfaces which can be used between
different CORBA implementations.

%package -n %{develname}
Summary:	Header files and libraries needed for libIDL development
Group:		Development/C
Conflicts:	ORBit-devel < 0.5.10
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{name}%{api_version}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}
Requires:	pkgconfig(glib-2.0)
Obsoletes:	%{mklibname -d  IDL 2 0} < 0.8.14-7

%description -n %{develname}
This package includes the header files and libraries needed for
developing or compiling programs using libIDL.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/*-config*

%files -n %{lib_name}
%doc AUTHORS README NEWS BUGS ChangeLog
%{_libdir}/libIDL-%{api_version}.so.%{lib_major}*

%files -n %{develname}
%doc tstidl.c
%{_bindir}/libIDL-config-2
%{_bindir}/*/libIDL-config-2
%{_includedir}/*
%{_infodir}/*.info*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*


%changelog
* Wed Jun 13 2012 Andrey Bondrov <abondrov@mandriva.org> 0.8.14-7
+ Revision: 805327
- Drop some legacy junk

* Thu Nov 10 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.8.14-6
+ Revision: 729635
- rebuild, cleaned up spec
  dropped .la & .a files

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.14-5
+ Revision: 661958
- rebuild

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.14-4
+ Revision: 661440
- fix deps
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.14-2mdv2011.0
+ Revision: 602515
- rebuild

* Tue Mar 30 2010 Götz Waschk <waschk@mandriva.org> 0.8.14-1mdv2010.1
+ Revision: 529213
- update to new version 0.8.14

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.13-3mdv2010.1
+ Revision: 520745
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.8.13-2mdv2010.0
+ Revision: 425510
- rebuild

* Tue Mar 17 2009 Götz Waschk <waschk@mandriva.org> 0.8.13-1mdv2009.1
+ Revision: 356776
- update to new version 0.8.13

* Tue Dec 02 2008 Götz Waschk <waschk@mandriva.org> 0.8.12-1mdv2009.1
+ Revision: 309223
- update to new version 0.8.12

* Tue Aug 19 2008 Götz Waschk <waschk@mandriva.org> 0.8.11-1mdv2009.0
+ Revision: 273748
- new version
- update license

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.8.10-2mdv2009.0
+ Revision: 222886
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Jan 29 2008 Götz Waschk <waschk@mandriva.org> 0.8.10-1mdv2008.1
+ Revision: 159761
- new version
- drop patch

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.8.9-3mdv2008.1
+ Revision: 150694
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Sep 24 2007 Frederic Crozat <fcrozat@mandriva.com> 0.8.9-2mdv2008.0
+ Revision: 92469
- Patch0 (SVN): fix ORBit2 build with gcc 4.2.2

* Mon Sep 17 2007 Götz Waschk <waschk@mandriva.org> 0.8.9-1mdv2008.0
+ Revision: 89092
- new version
- new devel name


* Mon Feb 26 2007 Götz Waschk <waschk@mandriva.org> 0.8.8-1mdv2007.0
+ Revision: 126029
- Import libIDL

* Mon Feb 26 2007 G�tz Waschk <waschk@mandriva.org> 0.8.8-1mdv2007.1
- new version

* Tue Jul 25 2006 Götz Waschk <waschk@mandriva.org> 0.8.7-1mdk
- New release 0.8.7

* Thu Feb 23 2006 Frederic Crozat <fcrozat@mandriva.com> 0.8.6-3mdk
- use mkrel

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.8.6-2mdk
- Rebuild

* Wed Jul 27 2005 G�tz Waschk <waschk@mandriva.org> 0.8.6-1mdk
- replace prereq
- reenable libtoolize
- New release 0.8.6

* Sat Feb 05 2005 Goetz Waschk <waschk@linux-mandrake.com> 0.8.5-1mdk
- New release 0.8.5

* Mon Jan 31 2005 G�tz Waschk <waschk@linux-mandrake.com> 0.8.4-2mdk
- multiarch support

* Wed Aug 18 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.8.4-1mdk
- fix source URL
- New release 0.8.4

