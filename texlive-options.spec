%global tl_name options
%global tl_revision 39030

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Provides convenient key-value options for LaTeX package writers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/options
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/options.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/options.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The options package provides easy to use key-value options for LaTeX
package writers. It has a similar interface as pgfkeys with path options
but comes with more built-in data types and more convenient support for
families and searching.

