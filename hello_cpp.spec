Name:           hello_cpp
Version:        0.1.0
Release:        0
License:        GPL-3.0
Summary:        Hello World in C++
Url:            https://github.com/openSUSE/example-obs
Group:          Development/Languages/C++
Source:         https://github.com/openSUSE/example-obs/release/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
Requires:       glibc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# BuildArch:

%description
This is an example project for the OBS documentation.

%prep
%setup -q -n %{name}-%{version}


%build
export CFLAGS="$RPM_OPT_FLAGS -DNDEBUG"
export CXXFLAGS="$RPM_OPT_FLAGS -DNDEBUG"

cmake -DCMAKE_INSTALL_PREFIX=/usr .
make %{?jobs:-j%jobs}


%install
make install DESTDIR="$RPM_BUILD_ROOT"


%files
%defattr(-,root,root,-)
%{_bindir}/*

%changelog
