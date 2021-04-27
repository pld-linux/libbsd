# TODO
# - take french bitstring.3 from fcron?
Summary:	Utility functions from BSD systems
Summary(pl.UTF-8):	Funkcje narzędziowe z systemów BSD
Name:		libbsd
Version:	0.11.3
Release:	1
License:	BSD, MIT (depending on part)
Group:		Libraries
Source0:	https://libbsd.freedesktop.org/releases/%{name}-%{version}.tar.xz
# Source0-md5:	5ce1707688d8bb75d365fadfce962b2c
URL:		https://libbsd.freedesktop.org/
BuildRequires:	libmd-bsd-devel >= 1.0
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libmd-bsd >= 1.0
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
Requires:	libmd-bsd >= 1.0
Conflicts:	glibc-devel < 6:2.19

%description devel
Header files for BSD library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki BSD.

%package static
Summary:	Static BSD library
Summary(pl.UTF-8):	Statyczna biblioteka BSD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Conflicts:	glibc-devel < 6:2.19

%description static
Static BSD library.

%description static -l pl.UTF-8
Statyczna biblioteka BSD.

%prep
%setup -q

%build
CPPFLAGS="%{rpmcppflags} -I/usr/include/libmd"
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libbsd.la

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
%attr(755,root,root) %{_libdir}/libbsd.so
%{_libdir}/libbsd-ctor.a
%{_includedir}/bsd
%{_pkgconfigdir}/libbsd.pc
%{_pkgconfigdir}/libbsd-ctor.pc
%{_pkgconfigdir}/libbsd-overlay.pc
%{_mandir}/man3/LIST_*.3bsd*
%{_mandir}/man3/RB_*.3bsd*
%{_mandir}/man3/SLIST_*.3bsd*
%{_mandir}/man3/SPLAY_*.3bsd*
%{_mandir}/man3/STAILQ_*.3bsd*
%{_mandir}/man3/TAILQ_*.3bsd*
%{_mandir}/man3/TIMESPEC_TO_TIMEVAL.3bsd*
%{_mandir}/man3/TIMEVAL_TO_TIMESPEC.3bsd*
%{_mandir}/man3/arc4random*.3bsd*
%{_mandir}/man3/be16dec.3bsd*
%{_mandir}/man3/be16enc.3bsd*
%{_mandir}/man3/be32dec.3bsd*
%{_mandir}/man3/be32enc.3bsd*
%{_mandir}/man3/be64dec.3bsd*
%{_mandir}/man3/be64enc.3bsd*
%{_mandir}/man3/bit_alloc.3bsd*
%{_mandir}/man3/bit_clear.3bsd*
%{_mandir}/man3/bit_decl.3bsd*
%{_mandir}/man3/bit_ffc.3bsd*
%{_mandir}/man3/bit_ffs.3bsd*
%{_mandir}/man3/bit_nclear.3bsd*
%{_mandir}/man3/bit_nset.3bsd*
%{_mandir}/man3/bit_set.3bsd*
%{_mandir}/man3/bit_test.3bsd*
%{_mandir}/man3/bitstr_size.3bsd*
%{_mandir}/man3/bitstring.3bsd*
%{_mandir}/man3/byteorder.3bsd*
%{_mandir}/man3/closefrom.3bsd*
%{_mandir}/man3/dehumanize_number.3bsd*
%{_mandir}/man3/errc.3bsd*
%{_mandir}/man3/expand_number.3bsd*
%{_mandir}/man3/explicit_bzero.3bsd*
%{_mandir}/man3/fgetln.3bsd*
%{_mandir}/man3/fgetwln.3bsd*
%{_mandir}/man3/flopen.3bsd*
%{_mandir}/man3/fmtcheck.3bsd*
%{_mandir}/man3/fparseln.3bsd*
%{_mandir}/man3/fpurge.3bsd*
%{_mandir}/man3/freezero.3bsd*
%{_mandir}/man3/funopen.3bsd*
%{_mandir}/man3/getbsize.3bsd*
%{_mandir}/man3/getmode.3bsd*
%{_mandir}/man3/getpeereid.3bsd*
%{_mandir}/man3/getprogname.3bsd*
%{_mandir}/man3/gid_from_group.3bsd*
%{_mandir}/man3/group_from_gid.3bsd*
%{_mandir}/man3/heapsort.3bsd*
%{_mandir}/man3/humanize_number.3bsd*
%{_mandir}/man3/le16dec.3bsd*
%{_mandir}/man3/le16enc.3bsd*
%{_mandir}/man3/le32dec.3bsd*
%{_mandir}/man3/le32enc.3bsd*
%{_mandir}/man3/le64dec.3bsd*
%{_mandir}/man3/le64enc.3bsd*
%{_mandir}/man3/md5.3bsd*
%{_mandir}/man3/mergesort.3bsd*
%{_mandir}/man3/nlist.3bsd*
%{_mandir}/man3/pidfile.3bsd*
%{_mandir}/man3/pidfile_close.3bsd*
%{_mandir}/man3/pidfile_open.3bsd*
%{_mandir}/man3/pidfile_remove.3bsd*
%{_mandir}/man3/pidfile_write.3bsd*
%{_mandir}/man3/pwcache.3bsd*
%{_mandir}/man3/queue.3bsd*
%{_mandir}/man3/radixsort.3bsd*
%{_mandir}/man3/readpassphrase.3bsd*
%{_mandir}/man3/reallocarray.3bsd*
%{_mandir}/man3/reallocf.3bsd*
%{_mandir}/man3/recallocarray.3bsd*
%{_mandir}/man3/setmode.3bsd*
%{_mandir}/man3/setproctitle.3bsd*
%{_mandir}/man3/setproctitle_init.3bsd*
%{_mandir}/man3/setprogname.3bsd*
%{_mandir}/man3/sl_add.3bsd*
%{_mandir}/man3/sl_delete.3bsd*
%{_mandir}/man3/sl_find.3bsd*
%{_mandir}/man3/sl_free.3bsd*
%{_mandir}/man3/sl_init.3bsd*
%{_mandir}/man3/sradixsort.3bsd*
%{_mandir}/man3/stringlist.3bsd*
%{_mandir}/man3/strlcat.3bsd*
%{_mandir}/man3/strlcpy.3bsd*
%{_mandir}/man3/strmode.3bsd*
%{_mandir}/man3/strnstr.3bsd*
%{_mandir}/man3/strnunvis.3bsd*
%{_mandir}/man3/strnvis.3bsd*
%{_mandir}/man3/strtoi.3bsd*
%{_mandir}/man3/strtonum.3bsd*
%{_mandir}/man3/strtou.3bsd*
%{_mandir}/man3/strunvis.3bsd*
%{_mandir}/man3/strvis.3bsd*
%{_mandir}/man3/strvisx.3bsd*
%{_mandir}/man3/timeradd.3bsd*
%{_mandir}/man3/timerclear.3bsd*
%{_mandir}/man3/timercmp.3bsd*
%{_mandir}/man3/timerisset.3bsd*
%{_mandir}/man3/timersub.3bsd*
%{_mandir}/man3/timespec.3bsd*
%{_mandir}/man3/timespecadd.3bsd*
%{_mandir}/man3/timespecclear.3bsd*
%{_mandir}/man3/timespeccmp.3bsd*
%{_mandir}/man3/timespecisset.3bsd*
%{_mandir}/man3/timespecsub.3bsd*
%{_mandir}/man3/timeval.3bsd*
%{_mandir}/man3/tree.3bsd*
%{_mandir}/man3/uid_from_user.3bsd*
%{_mandir}/man3/unvis.3bsd*
%{_mandir}/man3/user_from_uid.3bsd*
%{_mandir}/man3/vis.3bsd*
%{_mandir}/man3/wcslcat.3bsd*
%{_mandir}/man3/wcslcpy.3bsd*
%{_mandir}/man7/libbsd.7*

%files static
%defattr(644,root,root,755)
%{_libdir}/libbsd.a
