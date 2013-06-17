# -*- rpm-spec -*-

%define XEN_RELEASE %(test -z "${XEN_RELEASE}" && echo unknown || echo $XEN_RELEASE)

Summary: guest-templates - Create default XCP templates
Name:    guest-templates
Version: 0
Release: %{XEN_RELEASE}
Group:   System/Hypervisor
License: LGPL+linking exception
URL:  http://www.xen.org
Source0: guest-templates-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: ocaml, ocaml-findlib, ocaml-camlp4, ocaml-type-conv, ocaml-getopt, omake, xapi-client-devel, xapi-libs-devel

%description
This package contains a program which creates the default XCP templates, required by xapi at first boot time.

%prep 
%setup -q

%build
omake

%install
rm -rf %{buildroot}
DESTDIR=$RPM_BUILD_ROOT omake install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/opt/xensource/libexec/create_templates
/etc/firstboot.d/61-regenerate-old-templates


%changelog
