#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Starlet
%include	/usr/lib/rpm/macros.perl
Summary:	a simple, high-performance PSGI/Plack HTTP server
Name:		perl-Starlet
Version:	0.31
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/K/KA/KAZUHO/Starlet-%{version}.tar.gz
# Source0-md5:	b33a749d05b41aa0aca8fbe565965c4f
URL:		http://search.cpan.org/dist/Starlet/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Parallel::Prefork) >= 0.07
BuildRequires:	perl(Server::Starter) >= 0.06
BuildRequires:	perl-Plack >= 0.992
BuildRequires:	perl-Test-TCP >= 2.07
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Starlet is a standalone HTTP/1.1 web server.

%prep
%setup -q -n %{pdir}-%{version}

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
%doc Changes README
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/Starlet/
%{perl_vendorlib}/Plack/Handler/*.pm
%{_mandir}/man3/*
