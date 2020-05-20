Name:       python3-xdg
Summary:    The XDG Package for Python 3
Version:    0.26
Release:    1
License:    MIT
URL:        https://gitlab.freedesktop.org/xdg/pyxdg
Source0:    %{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
xdg is a Python module which provides the variables defined by
the XDG Base Directory Specification.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
%py3_build

%install
rm -rf %{buildroot}
%py3_install

%files
%license COPYING
%doc README
%{python3_sitelib}/*

