# fixme: should be defined in base system side
%define python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")

Name:       python3-xdg
Summary:    The XDG Package for Python 3
Version:    0.26
Release:    1
License:    MIT
URL:        https://gitlab.freedesktop.org/xdg/pyxdg
Source0:    %{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  python3-devel

%description
xdg is a Python module which provides the variables defined by
the XDG Base Directory Specification.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
%{__python3} setup.py build

%install
rm -rf %{buildroot}
%{__python3} setup.py install --skip-build --root %{buildroot}

%files
%license COPYING
%doc README
%{python3_sitearch}/*

