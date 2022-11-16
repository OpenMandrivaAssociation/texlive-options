Name:		texlive-options
Version:	39030
Release:	1
Summary:	Provides convenient key-value options for LaTeX package writers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/options
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/options.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/options.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The options package provides easy to use key-value options for
LaTeX package writers. It has a similar interface as pgfkeys
with path options but comes with more built-in data types and
more convenient support for families and searching.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/options
%doc %{_texmfdistdir}/doc/latex/options

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
