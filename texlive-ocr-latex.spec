%global tl_name ocr-latex
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX support for ocr fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ocr-latex
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ocr-latex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ocr-latex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package supports use of both ocr-a and ocr-b fonts in LaTeX
documents.

