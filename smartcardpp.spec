%define version 0.2.0
%define rel 1
%define release %mkrel %rel

%define realname smartcardpp

%define major 0
%define libname %mklibname %{realname} %major
%define libnamedev %mklibname %{realname} -d

Name:		smartcardpp
Version:	%{version}
Release:	%{release}
Summary:	A library for accessing smart cards

Group:		System/Libraries
License:	BSD
URL:		http://code.google.com/p/esteid
Source:		http://esteid.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	cmake
BuildRequires:	pcsc-lite-devel

%description
smartcardpp is a set of C++ classes to manage smart card
communications and implement basic command primitives.

%package	-n %{libname}
Summary:	A library for accessing smart cards
Group:		Development/Other
Requires:	%{_lib}pcsclite1

%description	-n %{libname}
smartcardpp is a set of C++ classes to manage smart card
communications and implement basic command primitives.

%package	-n %{libnamedev}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Requires:	pcsc-lite-devel

%description 	-n %{libnamedev}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ../..
popd

make -C %{_target_platform}/build


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT -C %{_target_platform}/build


%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%{_bindir}/card-test

%files -n %{libname}
%defattr(-,root,root,-)
%doc COPYING NEWS
%{_libdir}/*.so.*

%files -n %{libnamedev}
%defattr(-,root,root,-)
%{_includedir}/smartcardpp/
%{_libdir}/*.so


