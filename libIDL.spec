%define api_version	2
%define lib_major	0
%define lib_name	%mklibname IDL %{api_version} %{lib_major}
%define develname	%mklibname -d  IDL %{api_version}

Summary:	IDL parsing library
Name:		libIDL
Version:	0.8.14
Release:	7
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
Requires:	glib2-devel
Obsoletes:	%{mklibname -d  IDL 2 0}

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


