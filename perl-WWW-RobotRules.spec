#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	WWW
%define		pnam	RobotRules
Summary:	WWW::RobotRules - database of robots.txt-derived permissions
Summary(pl.UTF-8):	WWW::RobotRules - baza danych uprawnień z robots.txt
Name:		perl-WWW-RobotRules
Version:	6.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/WWW/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b7186e8b8b3701e70c22abf430742403
URL:		http://search.cpan.org/dist/WWW-RobotRules/
BuildRequires:	perl-devel >= 1:5.8.8
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-URI >= 1.10
%endif
Requires:	perl-URI >= 1.10
Conflicts:	perl-libwww < 6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module parses /robots.txt files as specified in "A Standard for
Robot Exclusion", at <http://www.robotstxt.org/wc/norobots.html>.
Webmasters can use the /robots.txt file to forbid conforming robots
from accessing parts of their web site.

The parsed files are kept in a WWW::RobotRules object, and this object
provides methods to check if access to a given URL is prohibited. The
same WWW::RobotRules object can be used for one or more parsed
/robots.txt files on any number of hosts.

%description -l pl.UTF-8
Ten moduł analizuje pliki /robots.txt opisane w dokumencie "A Standard
for Robot Exclusion" (<http://www.robotstxt.org/wc/norobots.html>).
Webmasterzy mogą używać pliku /robots.txt, aby zabronić automatom
zgodnym z tym standardem dostępu do pewnych plików na stronie WWW.

Przeanalizowane pliki są trzymane w obiekcie WWW::RobotRules, a obiekt
ten udostępnia metody do sprawdzania, czy dostęp do danego URL-a jest
zabroniony. Ten sam obiekt WWW::RobotRules może być używany dla
jednego lub większej liczby przeanalizowanych plików /robots.txt z
różnych hostów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/WWW/RobotRules.pm
%{perl_vendorlib}/WWW/RobotRules
%{_mandir}/man3/WWW::RobotRules*.3pm*
