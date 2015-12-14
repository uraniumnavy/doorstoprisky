Summary: Installs an older version of gcc that is ncurses compatible
Name: doorstoprisky
Version: 4.8.2
Release: 0.1.0
License: GNU GPL3
Group: Administrative
URL: http://ftp.gnu.org/gnu/gcc/gcc-4.8.2/gcc-4.8.2.tar.bz2
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  git libxml2-devel libjpeg-devel python gcc-c++ make openssl-devel gcc ruby ruby-devel rubygems tree nodejs npm ncurses ncurses-devel wget gmp-devel mpfr-devel libmpc-devel glibc-devel flex bison glibc-static

%description
The gcc that comes with fedora is not ncurses compatible.
This is an older version that is.

%prep
%setup -q

%build
mkdir build &&
cd build &&
../configure --disable-checking --enable-languages=c,c++ \
  --enable-multiarch --enable-shared --enable-threads=posix \
  --program-suffix=4.8 --with-gmp=/usr/local/lib --with-mpc=/usr/lib \
  --with-mpfr=/usr/lib --without-included-gettext --with-system-zlib \
  --with-tune=generic \
  --prefix=${RPM_BUILD_ROOT}/install/gcc-4.8.2 \
  --disable-multilib &&
make -j8 &&
true

%install
rm -rf ${RPM_BUILD_ROOT} &&
cd build &&
mkdir --parents ${RPM_BUILD_ROOT}/install/gcc-4.8.2 &&
make install &&
mkdir --parents ${RPMB_BUILD_ROOT}/usr/bin &&
ln -sf ${RPM_BUILD_ROOT}/install/gcc-4.8.2/bin/gcc ${RPM_BUILD_ROOT}/usr/bin/gcc &&
true


%clean
rm -rf $RPM_BUILD_ROOT


%files
/install/gcc-4.8.2
/usr/bin/gcc


%changelog
* Mon Dec 14 2015 vagrant <vagrant@localhost.localdomain> - 
- Initial build.

