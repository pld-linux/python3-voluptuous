#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Python data validation library
Summary(pl.UTF-8):	Biblioteka Pythona do sprawdzania poprawności danych
Name:		python3-voluptuous
Version:	0.16.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/voluptuous/
Source0:	https://files.pythonhosted.org/packages/source/v/voluptuous/voluptuous-%{version}.tar.gz
# Source0-md5:	3bb077be35ff17fc7b41ed3ab5856281
URL:		https://pypi.org/project/voluptuous/
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools
BuildRequires:	python3-wheel
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Voluptuous is a Python data validation library. It is primarily
intended for validating data coming into Python as JSON, YAML, etc.

%description -l pl.UTF-8
Voluptuous to biblioteka Pythona do sprawdzania poprawności danych.
Jest przeznaczona głównie do sprawdzania danych pochodzących z
formatów JSON, YAML itp.

%prep
%setup -q -n voluptuous-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest voluptuous/tests/tests.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md COPYING README.md
%{py3_sitescriptdir}/voluptuous
%{py3_sitescriptdir}/voluptuous-%{version}-py*.egg-info
