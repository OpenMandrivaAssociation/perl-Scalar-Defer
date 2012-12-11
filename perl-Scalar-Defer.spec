%define upstream_name    Scalar-Defer
%define upstream_version 0.23

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Lazy evaluation in Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Scalar/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::InsideOut)
BuildRequires:	perl(Exporter::Lite)
BuildArch:	noarch

%description
This module exports two functions, defer and lazy, for constructing values that
are evaluated on demand. It also exports a force function to force evaluation
of a deferred value.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL -n INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Scalar

%changelog
* Thu Feb 18 2010 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-1mdv2010.1
+ Revision: 507587
- update to 0.23

* Mon Feb 01 2010 Jérôme Quelin <jquelin@mandriva.org> 0.220.0-1mdv2010.1
+ Revision: 498985
- update to 0.22

* Tue Jan 19 2010 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-1mdv2010.1
+ Revision: 493488
- update to 0.21

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2010.0
+ Revision: 404360
- rebuild using %%perl_convert_version

* Thu Feb 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdv2009.1
+ Revision: 337803
- update to new version 0.20

* Fri Aug 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2009.0
+ Revision: 272312
- update to new version 0.18

* Wed Jul 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2009.0
+ Revision: 230638
- update to new version 0.16

* Mon Jun 30 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2009.0
+ Revision: 230280
- update to new version 0.15

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2008.1
+ Revision: 152906
- update to new version 0.14
- update to new version 0.14

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 20 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2008.1
+ Revision: 135951
- update to new version 0.12

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2008.1
+ Revision: 113254
- update to new version 0.11
- update to new version 0.11

* Wed Nov 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2008.1
+ Revision: 106608
- import perl-Scalar-Defer


* Tue Nov 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2008.1
- first mdv release 
