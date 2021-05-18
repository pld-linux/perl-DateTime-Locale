#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	DateTime
%define		pnam	Locale
Summary:	DateTime::Locale - localization support for DateTime
Summary(pl.UTF-8):	DateTime::Locale - wsparcie międzynarodowe dla DateTime
Name:		perl-DateTime-Locale
Version:	1.32
Release:	1
# same as perl 5 + Unicode for CLDR data
License:	GPL v1+ or Artistic with Unicode parts
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	23ba33ef2d40f349f213ed00680f86aa
URL:		https://metacpan.org/release/DateTime-Locale
BuildRequires:	perl-Dist-CheckConflicts >= 0.02
BuildRequires:	perl-File-ShareDir-Install >= 0.06
BuildRequires:	perl-devel >= 1:5.8.4
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-CPAN-Meta-Check >= 0.011
BuildRequires:	perl-CPAN-Meta-Requirements
BuildRequires:	perl-IPC-System-Simple
BuildRequires:	perl-Params-ValidationCompiler >= 0.13
BuildRequires:	perl-Path-Tiny
BuildRequires:	perl-Scalar-List-Utils >= 1.45
BuildRequires:	perl-Specio
BuildRequires:	perl-Storable
BuildRequires:	perl-Test-File-ShareDir
BuildRequires:	perl-Test-Simple >= 1.302015
BuildRequires:	perl-Test2-Suite
BuildRequires:	perl-Test2-Plugin-NoWarnings
BuildRequires:	perl-namespace-autoclean >= 0.19
%endif
BuildConflicts:	perl-DateTime-Format-Strptime <= 1.1000
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_perl	DateTime::Locale.*

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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/DateTime/Locale/*.pod

for f in $RPM_BUILD_ROOT%{perl_vendorlib}/auto/share/dist/DateTime-Locale/*.pl ; do
	basename=$(basename $f .pl)
	lang=$(echo $basename | sed -e 's/^en-\(US-POSIX\|[0-9]\+\).*//; s/-VALENCIA//; s/-[0-9][0-9][0-9]//; s/-[A-Z][a-z][a-z][a-z]//; s/^\([a-z][a-z][a-z]\?\)-\([A-Z][A-Z]\)$/\1_\2/')
	if [ -n "$lang" ]; then
		langtag="%lang($lang) "
	else
		langtag=
	fi
	echo "${langtag}%{perl_vendorlib}/auto/share/dist/DateTime-Locale/${basename}.pl"
	manname="$(echo "$basename" | tr - _)"
	echo "${langtag}%{_mandir}/man3/DateTime::Locale::${manname}.3pm*"
done > %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Changes LICENSE.cldr
%{perl_vendorlib}/DateTime/Locale.pm
%{perl_vendorlib}/DateTime/Locale
%dir %{perl_vendorlib}/auto/share/dist/DateTime-Locale
%{_mandir}/man3/DateTime::Locale.3pm*
%{_mandir}/man3/DateTime::Locale::Base.3pm*
%{_mandir}/man3/DateTime::Locale::Catalog.3pm*
%{_mandir}/man3/DateTime::Locale::Data.3pm*
%{_mandir}/man3/DateTime::Locale::FromData.3pm*
%{_mandir}/man3/DateTime::Locale::Util.3pm*
# generic man pages, without correspoding .pl files, so not caught by script
%lang(ar) %{_mandir}/man3/DateTime::Locale::ar.3pm*
%{_mandir}/man3/DateTime::Locale::en.3pm*
%{_mandir}/man3/DateTime::Locale::en_CA.3pm*
%{_mandir}/man3/DateTime::Locale::en_US.3pm*
%lang(es) %{_mandir}/man3/DateTime::Locale::es.3pm*
%lang(fr_FR) %{_mandir}/man3/DateTime::Locale::fr_FR.3pm*
%lang(hi) %{_mandir}/man3/DateTime::Locale::hi.3pm*
%lang(ja_JP) %{_mandir}/man3/DateTime::Locale::ja_JP.3pm*
%lang(pt_BR) %{_mandir}/man3/DateTime::Locale::pt_BR.3pm*
%lang(zh_CN) %{_mandir}/man3/DateTime::Locale::zh_Hans_CN.3pm*
%lang(zh_TW) %{_mandir}/man3/DateTime::Locale::zh_Hant_TW.3pm*
