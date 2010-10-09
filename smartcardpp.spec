%define version 0.2.0
%define rel 1
%define release %mkrel %rel

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

Requires:	libpcsclite1

Provides:	smartcardpp = %{version}-%{release}

%description
smartcardpp is a set of C++ classes to manage smart card
communications and implement basic command primitives.


%package	devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pcsc-lite-devel

Provides:	smartcardpp-devel = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ../..
popd

make %{?_smp_mflags} -C %{_target_platform}/build


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT -C %{_target_platform}/build


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc COPYING NEWS
%{_bindir}/card-test
%{_libdir}/*.so.*


%files devel
%defattr(-,root,root,-)
%{_includedir}/smartcardpp/
%{_libdir}/*.so


