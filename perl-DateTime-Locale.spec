#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DateTime
%define	pnam	Locale
Summary:	DateTime::Locale - Localization support for DateTime
Name:		perl-DateTime-Locale
Version:	0.09
Release:	1
# as perl itself
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e382e2bd7731b9ba79e6248bcf826ec1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Params-Validate
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains DateTime::Locale, an factory for the various
locale subclasses.  It also provides some functions for getting
information on available locales.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT 
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT
./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/DateTime/Locale*pm
%dir %{perl_vendorlib}/DateTime/Locale
%{perl_vendorlib}/DateTime/Locale/*.pm
%dir %{perl_vendorlib}/DateTime/Locale/Alias
%{perl_vendorlib}/DateTime/Locale/Alias/*pm
%{_mandir}/man3/*
