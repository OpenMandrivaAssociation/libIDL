%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_lto 1

%define api	2
%define major	0
%define libname	%mklibname IDL %{api} %{major}
%define devname	%mklibname -d  IDL %{api}

Summary:	IDL parsing library
Name:		libIDL
Version:	0.8.14
Release:	27
Url:		https://orbit-resource.sf.net/
License:	LGPLv2+
Group:		System/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libIDL/%{url_ver}/%{name}-%{version}.tar.bz2

BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	pkgconfig(glib-2.0)

%description
libIDL is a small library for creating parse trees of CORBA v2.2
compliant Interface Definition Language (IDL) files, which is a
specification for defining interfaces which can be used between
different CORBA implementations.

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
libIDL is a small library for creating parse trees of CORBA v2.2
compliant Interface Definition Language (IDL) files, which is a
specification for defining interfaces which can be used between
different CORBA implementations.

%package -n %{devname}
Summary:	Header files and libraries needed for libIDL development
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%{mklibname -d  IDL 2 0} < 0.8.14-7

%description -n %{devname}
This package includes the header files and libraries needed for
developing or compiling programs using libIDL.

%prep
%setup -q

%build
%configure \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libIDL-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS README NEWS BUGS ChangeLog
%doc tstidl.c
%{_bindir}/libIDL-config-2
%{_includedir}/*
%{_infodir}/*.info*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

