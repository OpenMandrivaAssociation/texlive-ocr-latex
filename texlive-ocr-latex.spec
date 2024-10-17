Name:		texlive-ocr-latex
Version:	15878
Release:	2
Summary:	LaTeX support for ocr fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ocr-latex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocr-latex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocr-latex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package supports use of both ocr-a and ocr-b fonts in LaTeX
documents.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ocr-latex/ocr.sty
%{_texmfdistdir}/tex/latex/ocr-latex/ot1oca.fd
%{_texmfdistdir}/tex/latex/ocr-latex/ot1ocra.fd
%{_texmfdistdir}/tex/latex/ocr-latex/ot1ocrb.fd
%{_texmfdistdir}/tex/latex/ocr-latex/ot1ocrbn.fd
%{_texmfdistdir}/tex/latex/ocr-latex/ot1ocrbns.fd
%{_texmfdistdir}/tex/latex/ocr-latex/ot1ocrbo.fd
%{_texmfdistdir}/tex/latex/ocr-latex/ot1ocrbs.fd
%doc %{_texmfdistdir}/doc/latex/ocr-latex/README
%doc %{_texmfdistdir}/doc/latex/ocr-latex/ocr.pdf
%doc %{_texmfdistdir}/doc/latex/ocr-latex/ocr.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
