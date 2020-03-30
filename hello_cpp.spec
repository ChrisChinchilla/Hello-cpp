Name:           hello_cpp
Version:        0.1.0
Release:        0
License:        MIT
Summary:        Hello World in C++
Url:            https://github.com/ChrisChinchilla/Hello-cpp
Group:          Development/Languages/C++
Source:         https://github.com/ChrisChinchilla/Hello-cpprelease/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
Requires:       glibc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A hello world in C++.

%setup -q -n %{name}-%{version}

%build
export CFLAGS="$RPM_OPT_FLAGS -DNDEBUG"
export CXXFLAGS="$RPM_OPT_FLAGS -DNDEBUG"
cmake -DCMAKE_INSTALL_PREFIX=/usr .
make %{?jobs:-j%jobs}

%install
make install DESTDIR="$RPM_BUILD_ROOT"

%defattr(-,root,root,-)
%{_bindir}/*

%changelog