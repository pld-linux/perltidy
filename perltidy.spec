# $Revision: 1.7 $
#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Perltidy is a tool to indent and reformat perl scripts
Summary(pl):	Perltidy jest narzêdziem do reformatowania skryptów perla
Name:		perltidy
Version:	20021130
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/%{name}/Perl-Tidy-%{version}.tar.gz
URL:		http://perltidy.sourceforge.net/
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perltidy reads a perl script and writes an indented, reformatted
script.

%description -l pl
Perltidy odczytuje skrypt perla i zapisuje go w postaci
zreformatowanej, z wciêciami.

%prep
%setup -q -n Perl-Tidy-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf examples/README
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README TODO
%{perl_sitelib}/Perl
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[13]/*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/[Rlt]*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/e*
