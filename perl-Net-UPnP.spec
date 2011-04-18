%define upstream_name    Net-UPnP
%define upstream_version 1.4.2

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Perl extension for UPnP
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz


BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


