#
# Conditional build:
%bcond_without	python	# Python binding
#
Summary:	Trace Format Babel Tower
Summary(pl.UTF-8):	Wieża Babel formatów narzędzi śledzących
Name:		babeltrace
Version:	1.5.7
Release:	1
License:	MIT
Group:		Applications/System
Source0:	https://www.efficios.com/files/babeltrace/%{name}-%{version}.tar.bz2
# Source0-md5:	41570da109988fcc1e7be90af0281a3c
Patch0:		%{name}-python.patch
URL:		http://diamon.org/babeltrace/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.22.0
BuildRequires:	libtool >= 2:2
BuildRequires:	libuuid-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
%{?with_python:BuildRequires:	python3-devel >= 1:3.2}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
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

%package -n python3-babeltrace
Summary:	Python 3 binding to Babeltrace library
Summary(pl.UTF-8):	Wiązanie Pythona 3 do biblioteki Babeltrace
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Obsoletes:	python-babeltrace < 1.5.3

%description -n python3-babeltrace
Python 3 binding to Babeltrace library.

%description -n python3-babeltrace -l pl.UTF-8
Wiązanie Pythona 3 do biblioteki Babeltrace.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_python:--enable-python-bindings} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# lib*.la kept - no .pc files for individual libraries

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/babeltrace

%if %{with python}
%py_postclean
%endif

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
%attr(755,root,root) %ghost %{_libdir}/libbabeltrace.so.1
%attr(755,root,root) %{_libdir}/libbabeltrace-ctf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbabeltrace-ctf.so.1
%attr(755,root,root) %{_libdir}/libbabeltrace-ctf-metadata.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbabeltrace-ctf-metadata.so.1
%attr(755,root,root) %{_libdir}/libbabeltrace-ctf-text.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbabeltrace-ctf-text.so.1
%attr(755,root,root) %{_libdir}/libbabeltrace-dummy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbabeltrace-dummy.so.1
%attr(755,root,root) %{_libdir}/libbabeltrace-lttng-live.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbabeltrace-lttng-live.so.1
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
%attr(755,root,root) %{_libdir}/libbabeltrace-lttng-live.so
%{_libdir}/libbabeltrace.la
%{_libdir}/libbabeltrace-ctf.la
%{_libdir}/libbabeltrace-ctf-metadata.la
%{_libdir}/libbabeltrace-ctf-text.la
%{_libdir}/libbabeltrace-dummy.la
%{_libdir}/libbabeltrace-lttng-live.la
%{_includedir}/babeltrace
%{_pkgconfigdir}/babeltrace.pc
%{_pkgconfigdir}/babeltrace-ctf.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libbabeltrace.a
%{_libdir}/libbabeltrace-ctf.a
%{_libdir}/libbabeltrace-ctf-metadata.a
%{_libdir}/libbabeltrace-ctf-text.a
%{_libdir}/libbabeltrace-dummy.a
%{_libdir}/libbabeltrace-lttng-live.a

%if %{with python}
%files -n python3-babeltrace
%defattr(644,root,root,755)
%dir %{py3_sitedir}/babeltrace
%attr(755,root,root) %{py3_sitedir}/babeltrace/_babeltrace.cpython-*.so
%{py3_sitedir}/babeltrace/*.py
%{py3_sitedir}/babeltrace/__pycache__
%{py3_sitedir}/babeltrace-%{version}-py*.egg-info
%endif
