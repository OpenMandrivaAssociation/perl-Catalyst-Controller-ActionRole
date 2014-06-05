%define upstream_name    Catalyst-Controller-ActionRole
%define upstream_version 0.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Apply roles to action instances

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Catalyst::Runtime)
BuildRequires: perl(Class::MOP)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Types::Moose)
BuildRequires: perl(String::RewritePrefix)
BuildRequires: perl(namespace::clean)
BuildRequires: perl-devel
BuildArch: noarch

%description
This module allows to apply roles to the 'Catalyst::Action's for different
controller methods.

For that a 'Does' attribute is provided. That attribute takes an argument,
that determines the role, which is going to be applied. If that argument is
prefixed with '+', it is assumed to be the full name of the role. If it's
prefixed with '~', the name of your application followed by
'::ActionRole::' is prepended. If it isn't prefixed with '+' or '~', the
role name will be searched for in '@INC' according to the rules for /ROLE
PREFIX SEARCHING.

Additionally it's possible to to apply roles to *all* actions of a
controller without specifying the 'Does' keyword in every action
definition:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*





