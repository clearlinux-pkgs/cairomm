#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cairomm
Version  : 1.16.1
Release  : 12
URL      : https://www.cairographics.org/releases/cairomm-1.16.1.tar.xz
Source0  : https://www.cairographics.org/releases/cairomm-1.16.1.tar.xz
Summary  : C++ binding for the cairo graphics library
Group    : Development/Tools
License  : LGPL-2.0
Requires: cairomm-lib = %{version}-%{release}
Requires: cairomm-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-meson
BuildRequires : doxygen
BuildRequires : graphviz
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(mm-common-libstdc++)
BuildRequires : pkgconfig(sigc++-3.0)

%description
cairomm
-------
This library provides a C++ interface to cairo.
See https://www.cairographics.org/cairomm/

%package dev
Summary: dev components for the cairomm package.
Group: Development
Requires: cairomm-lib = %{version}-%{release}
Provides: cairomm-devel = %{version}-%{release}
Requires: cairomm = %{version}-%{release}

%description dev
dev components for the cairomm package.


%package lib
Summary: lib components for the cairomm package.
Group: Libraries
Requires: cairomm-license = %{version}-%{release}

%description lib
lib components for the cairomm package.


%package license
Summary: license components for the cairomm package.
Group: Default

%description license
license components for the cairomm package.


%prep
%setup -q -n cairomm-1.16.1
cd %{_builddir}/cairomm-1.16.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1621555685
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/cairomm
cp %{_builddir}/cairomm-1.16.1/COPYING %{buildroot}/usr/share/package-licenses/cairomm/1679b0cb5406c6e4624f779c02e32985497f7aa7
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/cairomm-1.16/cairomm/cairomm.h
/usr/include/cairomm-1.16/cairomm/context.h
/usr/include/cairomm-1.16/cairomm/device.h
/usr/include/cairomm-1.16/cairomm/enums.h
/usr/include/cairomm-1.16/cairomm/exception.h
/usr/include/cairomm-1.16/cairomm/fontface.h
/usr/include/cairomm-1.16/cairomm/fontoptions.h
/usr/include/cairomm-1.16/cairomm/matrix.h
/usr/include/cairomm-1.16/cairomm/path.h
/usr/include/cairomm-1.16/cairomm/pattern.h
/usr/include/cairomm-1.16/cairomm/quartz_font.h
/usr/include/cairomm-1.16/cairomm/quartz_surface.h
/usr/include/cairomm-1.16/cairomm/refptr.h
/usr/include/cairomm-1.16/cairomm/region.h
/usr/include/cairomm-1.16/cairomm/scaledfont.h
/usr/include/cairomm-1.16/cairomm/script.h
/usr/include/cairomm-1.16/cairomm/script_surface.h
/usr/include/cairomm-1.16/cairomm/surface.h
/usr/include/cairomm-1.16/cairomm/types.h
/usr/include/cairomm-1.16/cairomm/win32_font.h
/usr/include/cairomm-1.16/cairomm/win32_surface.h
/usr/include/cairomm-1.16/cairomm/xlib_surface.h
/usr/lib64/cairomm-1.16/include/cairommconfig.h
/usr/lib64/libcairomm-1.16.so
/usr/lib64/pkgconfig/cairomm-1.16.pc
/usr/lib64/pkgconfig/cairomm-ft-1.16.pc
/usr/lib64/pkgconfig/cairomm-pdf-1.16.pc
/usr/lib64/pkgconfig/cairomm-png-1.16.pc
/usr/lib64/pkgconfig/cairomm-ps-1.16.pc
/usr/lib64/pkgconfig/cairomm-svg-1.16.pc
/usr/lib64/pkgconfig/cairomm-xlib-1.16.pc
/usr/lib64/pkgconfig/cairomm-xlib-xrender-1.16.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcairomm-1.16.so.1
/usr/lib64/libcairomm-1.16.so.1.4.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cairomm/1679b0cb5406c6e4624f779c02e32985497f7aa7
