#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DateTime
%define		pnam	Locale
Summary:	DateTime::Locale - localization support for DateTime
Summary(pl):	DateTime::Locale - wsparcie miêdzynarodowe dla DateTime
Name:		perl-DateTime-Locale
Version:	0.21
Release:	1
# same as perl (parts on ICU License)
License:	GPL v1+ or Artistic (parts on ICU License)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	57b7717cc5a1ff34efedcfe3414d2ed4
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DateTime
BuildRequires:	perl-File-Find-Rule
BuildRequires:	perl-Test-Pod >= 0.95
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains DateTime::Locale, an factory for the various
locale subclasses.  It also provides some functions for getting
information on available locales.

%description -l pl
Pakiet ten zawiera DateTime::Locale, ¼ród³o ró¿nych klas zwi±zanych z
umiêdzynarodowieniem. Udostêpnia równie¿ pewne funkcje s³u¿±ce do
pobierania informacji o dostêpnych locale.

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
%doc Changes README LICENSE.icu
%{perl_vendorlib}/DateTime/Locale*pm
%dir %{perl_vendorlib}/DateTime/Locale
%{perl_vendorlib}/DateTime/Locale/*.pm
%dir %{perl_vendorlib}/DateTime/Locale/Alias
%{perl_vendorlib}/DateTime/Locale/Alias/*pm
%{_mandir}/man3/*
