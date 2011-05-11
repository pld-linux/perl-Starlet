#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Starlet
%include	/usr/lib/rpm/macros.perl
Summary:	a simple, high-performance PSGI/Plack HTTP server
#Summary(pl.UTF-8):	
Name:		perl-Starlet
Version:	0.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/K/KA/KAZUHO/Starlet-0.13.tar.gz
# Source0-md5:	222eff2e8e5d69a44a8a3935fb8837cd
URL:		http://search.cpan.org/dist/Starlet/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Parallel::Prefork) >= 0.07
BuildRequires:	perl(Server::Starter) >= 0.06
BuildRequires:	perl-Plack >= 0.992
BuildRequires:	perl-Test-TCP >= 0.15
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description


# %description -l pl.UTF-8
# TODO

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
%{perl_vendorlib}/Plack/Server/Standalone/Prefork
%{_mandir}/man3/*
