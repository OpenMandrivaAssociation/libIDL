%define api_version	2
%define lib_major	0
%define lib_name	%mklibname IDL %{api_version} %{lib_major}
%define develname %mklibname -d  IDL %{api_version}

Summary:	IDL parsing library
Name:		libIDL
Version: 0.8.9
Release:	%mkrel 3
URL:		http://orbit-resource.sf.net/
License:	LGPL
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
# (fc) 0.8.9-2mdv fix ORBit2 build with gcc4.2 (SVN)
Patch0:		libIDL-0.8.9-fixgcc42.patch

BuildConflicts: ORBit-devel < 0.5.10
BuildRequires:	flex bison pkgconfig
BuildRequires:  libglib2.0-devel

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

%package -n %develname
Summary:	Header files and libraries needed for libIDL development
Group:		Development/C
Conflicts:	ORBit-devel < 0.5.10
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{name}%{api_version}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}
Requires:   glib2-devel
Requires(post,preun): info-install
Obsoletes: %mklibname -d  IDL 2 0

%description -n %develname
This package includes the header files and libraries needed for
developing or compiling programs using libIDL.

%prep
%setup -q
%patch0 -p1 -b .gcc42

%build

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std
%multiarch_binaries %buildroot%_bindir/*-config*

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%post -n %develname
%_install_info %{name}2.info

%preun -n %develname
%_remove_install_info %{name}2.info

%clean
rm -rf %{buildroot}

%files -n %{lib_name}
%defattr(-,root,root)
%doc AUTHORS README NEWS BUGS ChangeLog
%{_libdir}/libIDL-%{api_version}.so.%{lib_major}*

%files -n %develname
%defattr(-,root,root)
%doc tstidl.c
%{_bindir}/libIDL-config-2
%{_bindir}/*/libIDL-config-2
%{_includedir}/*
%{_infodir}/*.info*
%{_libdir}/lib*.la
%{_libdir}/lib*.a
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*


