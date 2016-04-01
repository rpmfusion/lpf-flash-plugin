# Binary package, no debuginfo should be generated
%global         debug_package %{nil}

# %%global will not work here, lazy evaluation needed.
%define         target_pkg %(t=%{name}; echo ${t#lpf-})

Name:           lpf-flash-plugin
Version:        11.2.202.577
Release:        1%{?dist}
Epoch:          1
Summary:        Adobe Flash Player package bootstrap

License:        MIT
URL:            http://github.com/leamas/lpf
Group:          Development/Tools
ExclusiveArch:  %{ix86} x86_64

Source0:        flash-plugin.spec.in
Source1:        README
Source2:        LICENSE

BuildRequires:  desktop-file-utils
BuildRequires:  lpf
Requires:       lpf

%description
Bootstrap package allowing the lpf system to build the non-redistributable
flash-plugin package.

The flash-plugin package is available only for i686 and x86_64 systems.

%prep
%setup -cT
cp %{SOURCE1} README
cp %{SOURCE2} LICENSE


%build


%install
# lpf-setup-pkg [-a arch] [-e eula] <topdir> <specfile> [sources...]
/usr/share/lpf/scripts/lpf-setup-pkg %{buildroot} %{SOURCE0}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%post
DISPLAY= lpf scan 2>/dev/null || :

%postun
if [ "$1" = '0' ]; then
    /usr/share/lpf/scripts/lpf-pkg-postun %{target_pkg} &>/dev/null || :
fi

%triggerpostun -- %{target_pkg}
if [ "$2" = '0' ]; then
    lpf scan-removal %{target_pkg} &>/dev/null || :
fi


%files
%doc README LICENSE
/usr/share/applications/%{name}.desktop
/usr/share/lpf/packages/%{target_pkg}
%attr(775,pkg-build,pkg-build) /var/lib/lpf/packages/%{target_pkg}
%attr(664,pkg-build,pkg-build) /var/lib/lpf/packages/%{target_pkg}/state


%changelog
* Fri Apr 01 2016 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.577-1
- Update to 11.2.202.577.

* Wed Feb 24 2016 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.569-1
- Update to 11.2.202.569.

* Fri Nov 20 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.548-1
- Update to latest 11.2.202.548.

* Wed Jun 24 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.468-1
- Update to 11.2.202.468.

* Tue May 12 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.460-1
- Update to 11.2.202.460.

* Fri Apr 24 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.457-1
- Update to 11.2.202.457.

* Mon Mar 30 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.451-1
- Update to 11.2.202.451.

* Thu Feb 05 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.442-1
- Update to version 11.2.202.442.

* Thu Jan 29 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.440-1
- Update to 11.2.202.440.

* Fri Jan 23 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.438-1
- Update to 11.2.202.438.

* Sun Dec 14 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.425-1
- Update to 11.2.202.425.

* Thu Oct 30 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.411-1
- Update to 11.2.202.411.

* Wed Sep 10 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.406-1
- Update to 11.2.202.406.

* Wed Jul 09 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.394-1
- Update to 11.2.202.394.

* Mon Jun 16 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.378-1
- Update to 11.2.202.378.

* Mon May 19 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.359-2
- Update to 11.2.202.359.

* Wed Apr 30 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.356-1
- Update to 11.2.202.356.

* Fri Mar 14 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.346-1
- Update to 11.2.202.346.

* Mon Mar 10 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.341-1
- Update to 11.2.202.341.

* Sun Feb 09 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.336-1
- Update to 11.2.202.336.

* Wed Jan 29 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.335-1
- Update to 11.2.202.335.

* Thu Jan 09 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.332-2
- Bump release to add missing README in CVS.

* Mon Dec 16 2013 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.332-1
- Updated to 11.2.202.332.

* Wed Nov 27 2013 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.327-4
- Updated postun and triggerpostun sections as per latest specifications.

* Tue Nov 26 2013 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.327-3
- Add triggerpostun section, update description.
- Updated lpf-flash-plugin.spec.in.

* Mon Nov 25 2013 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.327-2
- Updated install, post and postun sections for the latest additions.

* Thu Nov 21 2013 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.327-1
- First build.
