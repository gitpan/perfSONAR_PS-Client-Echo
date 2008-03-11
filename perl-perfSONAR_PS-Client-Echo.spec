Name:           perl-perfSONAR_PS-Client-Echo
Version:        0.06
Release:        1%{?dist}
Summary:        perfSONAR_PS::Client::Echo Perl module
License:        distributable, see LICENSE
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/perfSONAR_PS-Client-Echo/
Source0:        http://www.cpan.org/modules/by-module/perfSONAR_PS/perfSONAR_PS-Client-Echo-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       perl(Log::Log4perl) >= 1
Requires:       perl(perfSONAR_PS::Common) >= 0.06
Requires:       perl(perfSONAR_PS::Messages) >= 0.06
Requires:       perl(perfSONAR_PS::Transport) >= 0.06
Requires:       perl(perfSONAR_PS::XML::Document_string) >= 0.06
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
perfSONAR_PS::Client::Echo is a module that provides an OO interface to perform
perfSONAR ping requests against perfSONAR services.

%prep
%setup -q -n perfSONAR_PS-Client-Echo-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null \;

chmod -R u+rwX,go+rX,go-w $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README modules perl-perfSONAR_PS-Client-Echo.spec psping
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Feb 28 2008 aaron@internet2.edu 0.06-1
- Specfile autogenerated.