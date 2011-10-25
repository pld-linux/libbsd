Summary:	Utility functions from BSD systems
Summary(pl.UTF-8):	Funkcje narzędziowe z systemów BSD
Name:		libbsd
Version:	0.3.0
Release:	1
License:	BSD, MIT (depending on part)
Group:		Libraries
Source0:	http://libbsd.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	833e58531b4bd84b119b53d834d8e0d8
URL:		http://libbsd.freedesktop.org/
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides useful functions commonly found on BSD systems,
and lacking on others like GNU systems, thus making it easier to port
projects with strong BSD origins, without needing to embed the same
code over and over again on each project.

%description -l pl.UTF-8
Ta biblioteka udostępnia funkcje zwykle spotykane w systemach BSD, a
nie występujące na innych, takich jak systemy GNU. Dzięki temu ułatwia
portowanie projektów mających silne korzenie BSD bez potrzeby
osadzania ciągle tego samego kodu w każdym projekcie.

%package devel
Summary:	Header files for BSD library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki BSD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for BSD library.

Note: to avoid clash with libbsd.a from glibc, library provided by
this package is available as -lbsdutil.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki BSD.

Uwaga: aby zapobiec konfliktowi z libbsd.a z glibc, biblioteka
dostarczana przez ten pakiet jest dostępna jako -lbsdutil.

%package static
Summary:	Static BSD library
Summary(pl.UTF-8):	Statyczna biblioteka BSD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static BSD library.

Note: to avoid clash with libbsd.a from glibc, library provided by
this package is available as libbsdutil.a.

%description static -l pl.UTF-8
Statyczna biblioteka BSD.

Uwaga: aby zapobiec konfliktowi z libbsd.a z glibc, biblioteka
dostarczana przez ten pakiet jest dostępna jako libbsdutil.a.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

# Makefile defaults to install shared library to /lib, but in PLD it's not needed currently
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	exec_prefix=%{_prefix} \
	libdir=%{_libdir} \
	usrlibdir=%{_libdir}

# avoid clash of deprecated headers with other packages
%{__rm} $RPM_BUILD_ROOT%{_includedir}/{libutil,nlist,vis}.h

# avoid clash with libbsd.a from glibc
mv $RPM_BUILD_ROOT%{_libdir}/{libbsd,libbsdutil}.so
mv $RPM_BUILD_ROOT%{_libdir}/{libbsd,libbsdutil}.a
sed -i -e 's/-lbsd/-lbsdutil/' $RPM_BUILD_ROOT%{_pkgconfigdir}/*.pc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libbsd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbsd.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbsdutil.so
%{_includedir}/bsd
%{_pkgconfigdir}/libbsd.pc
%{_pkgconfigdir}/libbsd-overlay.pc
%{_mandir}/man3/arc4random*.3*
%{_mandir}/man3/dehumanize_number.3*
%{_mandir}/man3/fgetln.3*
%{_mandir}/man3/flopen.3*
%{_mandir}/man3/fmtcheck.3*
%{_mandir}/man3/getmode.3*
%{_mandir}/man3/getpeereid.3*
%{_mandir}/man3/heapsort.3*
%{_mandir}/man3/humanize_number.3*
%{_mandir}/man3/md5.3bsd*
%{_mandir}/man3/mergesort.3*
%{_mandir}/man3/nlist.3*
%{_mandir}/man3/pidfile.3*
%{_mandir}/man3/radixsort.3*
%{_mandir}/man3/readpassphrase.3*
%{_mandir}/man3/reallocf.3*
%{_mandir}/man3/setmode.3*
%{_mandir}/man3/sradixsort.3*
%{_mandir}/man3/strlcat.3*
%{_mandir}/man3/strlcpy.3*
%{_mandir}/man3/strmode.3*
%{_mandir}/man3/strtonum.3*
%{_mandir}/man3/unvis.3*
%{_mandir}/man3/vis.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libbsdutil.a
