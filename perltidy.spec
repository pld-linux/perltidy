#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Perl
%define		pnam	Tidy
%include	/usr/lib/rpm/macros.perl
Summary:	Perltidy - a tool to indent and reformat Perl scripts
Summary(pl.UTF-8):	Perltidy - narzędzie do reformatowania skryptów Perla
Name:		perltidy
Version:	20181119
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://www.cpan.org/modules/by-module/Perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6503132f8ef74ddf54cbe69e1d9f2f47
Patch0:		%{name}-makefile.patch
URL:		http://perltidy.sourceforge.net/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perltidy reads a Perl script and writes an indented, reformatted
script.

%description -l pl.UTF-8
Perltidy odczytuje skrypt Perla i zapisuje go w postaci
zreformatowanej, z wcięciami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf examples/README
cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__rm} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/pt.bat
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Perl/Tidy.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS.md CHANGES.md COPYING INSTALL.md README.md
%attr(755,root,root) %{_bindir}/perltidy
%{perl_vendorlib}/Perl/Tidy.pm
%{_mandir}/man1/perltidy.1p*
%{_mandir}/man3/Perl::Tidy.3pm*
%{_mandir}/man3/Perl::Tidy::Formatter.3pm*
%{perl_vendorlib}/Perl/Tidy
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/README.gz
%{_examplesdir}/%{name}-%{version}/filter_example.in
%{_examplesdir}/%{name}-%{version}/lextest
%{_examplesdir}/%{name}-%{version}/test*.t
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
