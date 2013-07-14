Summary:	Trace Format Babel Tower
Summary(pl.UTF-8):	Wieża Babel formatów narzędzi śledzących
Name:		babeltrace
Version:	1.1.1
Release:	1
License:	MIT
Group:		Applications/System
Source0:	http://lttng.org/files/babeltrace/%{name}-%{version}.tar.bz2
# Source0-md5:	15cf79cb2407a75874e41c9e7658f987
URL:		http://lttng.org/babeltrace
BuildRequires:	glib2-devel >= 1:2.22.0
BuildRequires:	libuuid-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
Requires:	glib2 >= 1:2.22.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project provides trace read and write libraries, as well as a
trace converter. A plugin can be created for any trace format to allow
its conversion to/from another trace format.

%description -l pl.UTF-8
Ten projekt udostępnia biblioteki do odczytu i zapisu śladów, a także
konwerter śladów. Można tworzyć wtyczki dla dowolnego formatu śladów,
aby umożliwić konwersję do/z innego formatu.

%package devel
Summary:	Header files for Babeltrace libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Babeltrace
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.22.0
Requires:	libuuid-devel
Requires:	popt-devel

%description devel
Header files for Babeltrace libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Babeltrace.

%package static
Summary:	Static Babeltrace libraries
Summary(pl.UTF-8):	Statyczne biblioteki Babeltrace
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Babeltrace libraries.

%description static -l pl.UTF-8
Statyczne biblioteki Babeltrace.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# *.la kept - no .pc files for individual libraries

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/babeltrace

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README std-ext-lib.txt
%attr(755,root,root) %{_bindir}/babeltrace
%attr(755,root,root) %{_bindir}/babeltrace-log
%attr(755,root,root) %{_libdir}/libbabeltrace.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbabeltrace.so.0
%attr(755,root,root) %{_libdir}/libbabeltrace-ctf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbabeltrace-ctf.so.0
%attr(755,root,root) %{_libdir}/libbabeltrace-ctf-metadata.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbabeltrace-ctf-metadata.so.0
%attr(755,root,root) %{_libdir}/libbabeltrace-ctf-text.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbabeltrace-ctf-text.so.0
%attr(755,root,root) %{_libdir}/libbabeltrace-dummy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbabeltrace-dummy.so.0
%{_mandir}/man1/babeltrace.1*
%{_mandir}/man1/babeltrace-log.1*

%files devel
%defattr(644,root,root,755)
%doc doc/{API,development}.txt
%attr(755,root,root) %{_libdir}/libbabeltrace.so
%attr(755,root,root) %{_libdir}/libbabeltrace-ctf.so
%attr(755,root,root) %{_libdir}/libbabeltrace-ctf-metadata.so
%attr(755,root,root) %{_libdir}/libbabeltrace-ctf-text.so
%attr(755,root,root) %{_libdir}/libbabeltrace-dummy.so
%{_libdir}/libbabeltrace.la
%{_libdir}/libbabeltrace-ctf.la
%{_libdir}/libbabeltrace-ctf-metadata.la
%{_libdir}/libbabeltrace-ctf-text.la
%{_libdir}/libbabeltrace-dummy.la
%{_includedir}/babeltrace
%{_pkgconfigdir}/babeltrace.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libbabeltrace.a
%{_libdir}/libbabeltrace-ctf.a
%{_libdir}/libbabeltrace-ctf-metadata.a
%{_libdir}/libbabeltrace-ctf-text.a
%{_libdir}/libbabeltrace-dummy.a
