%define upstream_name    Scalar-Defer
%define upstream_version 0.22

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Lazy evaluation in Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Scalar/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Class::InsideOut)
BuildRequires:  perl(Exporter::Lite)
BuildArch:      noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}

%description
This module exports two functions, defer and lazy, for constructing values that
are evaluated on demand. It also exports a force function to force evaluation
of a deferred value.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL -n INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Scalar
