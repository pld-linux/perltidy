# $Revision: 1.1 $
%include	/usr/lib/rpm/macros.perl
Summary:	Perltidy is a tool to indent and reformat perl scripts.
Summary(pl):	Perltidy jest narzêdziem do reformatowanie skryptów perla.
Name:		perltidy
Version:	20020225
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://prdownloads.sourceforge.net/%{name}/Perl-Tidy-%{version}.tgz
URL:		http://perltidy.sourceforge.net/
BuildRequires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perltidy reads a perl script and writes an indented, reformatted script.

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

gzip -9nf BUGS CHANGES COPYING INSTALL README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%doc examples
%doc %{_mandir}/man[13]/*
%{perl_sitelib}/Perl/Tidy.pm
%attr(755,root,root) %{_bindir}/*
