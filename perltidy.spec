# $Revision: 1.3 $
%include	/usr/lib/rpm/macros.perl
Summary:	Perltidy is a tool to indent and reformat perl scripts
Summary(pl):	Perltidy jest narzêdziem do reformatowania skryptów perla
Name:		perltidy
Version:	20020225
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://prdownloads.sourceforge.net/%{name}/Perl-Tidy-%{version}.tgz
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
perl Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf BUGS CHANGES README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz examples
%{perl_sitelib}/Perl/Tidy.pm
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[13]/*
