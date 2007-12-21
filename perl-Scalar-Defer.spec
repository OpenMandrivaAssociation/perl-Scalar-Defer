%define module   Scalar-Defer

Name:		perl-%{module}
Version:    0.12
Release:    %mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Lazy evaluation in Perl
Url:		    http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Scalar/%{module}-%{version}.tar.gz
BuildRequires:  perl(Class::InsideOut)
BuildRequires:  perl(Exporter::Lite)
BuildArch:      noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
This module exports two functions, defer and lazy, for constructing values that
are evaluated on demand. It also exports a force function to force evaluation
of a deferred value.

%prep
%setup -q -n %{module}-%{version} 

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

