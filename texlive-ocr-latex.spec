Name:		texlive-ocr-latex
Version:	20070311
Release:	1
Summary:	LaTeX support for ocr fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ocr-latex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocr-latex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocr-latex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package supports use of both ocr-a and ocr-b fonts in LaTeX
documents.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
