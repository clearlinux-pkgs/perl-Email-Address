#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Email-Address
Version  : 1.913
Release  : 29
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Address-1.913.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Address-1.913.tar.gz
Summary  : 'RFC 2822 Address Parsing and Creation'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Email-Address-license = %{version}-%{release}
Requires: perl-Email-Address-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Email-Address,
version 1.913:
RFC 2822 Address Parsing and Creation

%package dev
Summary: dev components for the perl-Email-Address package.
Group: Development
Provides: perl-Email-Address-devel = %{version}-%{release}
Requires: perl-Email-Address = %{version}-%{release}

%description dev
dev components for the perl-Email-Address package.


%package license
Summary: license components for the perl-Email-Address package.
Group: Default

%description license
license components for the perl-Email-Address package.


%package perl
Summary: perl components for the perl-Email-Address package.
Group: Default
Requires: perl-Email-Address = %{version}-%{release}

%description perl
perl components for the perl-Email-Address package.


%prep
%setup -q -n Email-Address-1.913
cd %{_builddir}/Email-Address-1.913

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Email-Address
cp %{_builddir}/Email-Address-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Email-Address/f1a26472dd8cb0b518c04e663edd0f640ce669a5 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Email::Address.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Email-Address/f1a26472dd8cb0b518c04e663edd0f640ce669a5

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
