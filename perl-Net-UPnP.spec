%define upstream_name    Net-UPnP
%define upstream_version 1.4.2

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl extension for UPnP
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel

BuildArch:	noarch

%description
This package provides some functions to control UPnP devices.

Currently, the package provides only functions for the control point. To
control UPnP devices, see the Net::UPnP::ControlPoint manpage.

As a sample of the control point, the package provides the
Net::UPnP::AV::MediaServer manpage to control the devices such as DLNA
media servers. As the example, please dms2vodcast.pl that converts from the
MPEG2 movies to the MPEG4 one and outputs the RSS file for Vodcasting.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.4.2-2mdv2011.0
+ Revision: 655146
- rebuild for updated spec-helper

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - import perl-Net-UPnP


* Fri Jul 23 2010 cpan2dist 1.4.2-1mdv
- initial mdv release, generated with cpan2dist
