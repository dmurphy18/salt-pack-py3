%global pypi_name funcsigs

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_without python3
%endif

%bcond_with python2
%bcond_without python3

%bcond_with tests
%bcond_with docs


Name:           python-%{pypi_name}
Version:        1.0.2
Release:        13%{?dist}
Summary:        Python function signatures from PEP362 for Python 2.6, 2.7 and 3.2+

License:        ASL 2.0
URL:            https://github.com/testing-cabal/funcsigs?
Source0:        https://pypi.io/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-sphinx
BuildRequires:  python2-unittest2
%endif

%description
funcsigs is a backport of the PEP 362 function signature features from
Python 3.3's inspect module. The backport is compatible with Python 2.6, 2.7
as well as 3.2 and up.


%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        Python function signatures from PEP362 for Python 2.6, 2.7 and 3.2+
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
funcsigs is a backport of the PEP 362 function signature features from
Python 3.3's inspect module. The backport is compatible with Python 2.6, 2.7
as well as 3.2 and up.
%endif


%if %{with python3}
%package -n     python3-%{pypi_name}
Summary:        Python function signatures from PEP362 for Python 2.6, 2.7 and 3.2+
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-unittest2
%endif

%description -n python3-%{pypi_name}
funcsigs is a backport of the PEP 362 function signature features from
Python 3.3's inspect module. The backport is compatible with Python 2.6, 2.7
as well as 3.2 and up.
%endif

%if %{with docs}
%package -n python-%{pypi_name}-doc
Summary:        funcsigs documentation
%description -n python-%{pypi_name}-doc
Documentation for funcsigs
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%if 0%{?rhel} && 0%{?rhel} == 7
sed -i '/extras_require/,+3d' setup.py
%endif

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%if %{with docs}
# generate html docs
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%if %{with python3}
%py3_install
%endif

%if %{with python2}
%py2_install
%endif


%if %{with tests}
%check
%if %{with python2}
%{__python2} setup.py test
%endif
%if %{with python3}
%{__python3} setup.py test
%endif
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%if %{with docs}
%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
%endif

%changelog
* Thu May 09 2019 SaltStack Packaging Team <packaging@saltstack.com> - 1.0.2-13
- Added support for Redhat 8, and support for Python 2 packages optional

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-10
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.2-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 1.0.2-7
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 1.0.2-4
- Enable tests

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.0.2-3
- Rebuild for Python 3.6
- Disable python3 tests for now

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Jun 11 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.0.2-1
- Upstream 1.0.2 (RHBZ#1341262)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec  4 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 0.4-2
- Add license file in doc subpackage

* Wed Dec 02 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 0.4-1
- Initial package.