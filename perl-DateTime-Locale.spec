#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	DateTime
%define		pnam	Locale
%include	/usr/lib/rpm/macros.perl
Summary:	DateTime::Locale - localization support for DateTime
Summary(pl.UTF-8):	DateTime::Locale - wsparcie międzynarodowe dla DateTime
Name:		perl-DateTime-Locale
Version:	1.11
Release:	1
License:	GPL v1+ or Artistic (parts on ICU License)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DateTime/DROLSKY/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e842b6c61739d603917cea330555eb31
URL:		http://search.cpan.org/dist/DateTime-Locale/
BuildRequires:	perl-Dist-CheckConflicts >= 0.02
BuildRequires:	perl-devel >= 1:5.8.4
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-CPAN-Meta-Check >= 0.011
BuildRequires:	perl-CPAN-Meta-Requirements
BuildRequires:	perl-File-Find-Rule
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-Params-ValidationCompiler >= 0.13
BuildRequires:	perl-Scalar-List-Utils >= 1.45
BuildRequires:	perl-Specio
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Pod >= 1.41
BuildRequires:	perl-Test-Simple >= 0.96
BuildRequires:	perl-Test-Requires
BuildRequires:	perl-Test-Warnings
BuildRequires:	perl-namespace-autoclean >= 0.19
%endif
BuildConflicts:	perl-DateTime-Format-Strptime <= 1.1000
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_perl	DateTime::Locale.*)

%description
This package contains DateTime::Locale, an factory for the various
locale subclasses. It also provides some functions for getting
information on available locales.

%description -l pl.UTF-8
Pakiet ten zawiera DateTime::Locale, źródło różnych klas związanych z
umiędzynarodowieniem. Udostępnia również pewne funkcje służące do
pobierania informacji o dostępnych locale.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorlib}/DateTime/Locale.pm
%{perl_vendorlib}/DateTime/Locale
%{_mandir}/man3/DateTime::Locale*.3pm*
