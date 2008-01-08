#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Perltidy - a tool to indent and reformat Perl scripts
Summary(pl.UTF-8):	Perltidy - narzędzie do reformatowania skryptów Perla
Name:		perltidy
Version:	20071205
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/%{name}/Perl-Tidy-%{version}.tar.gz
# Source0-md5:	d9d2e7659fe6f9e4e5d6d329eb3393dd
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
%setup -q -n Perl-Tidy-%{version}

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
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README TODO
%{perl_vendorlib}/Perl
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[13]/*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/[Rlt]*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
