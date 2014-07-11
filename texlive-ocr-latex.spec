# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/ocr-latex
# catalog-date 2007-03-11 14:06:37 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-ocr-latex
Version:	20070311
Release:	8
Summary:	LaTeX support for ocr fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ocr-latex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocr-latex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocr-latex.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070311-2
+ Revision: 754502
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070311-1
+ Revision: 719152
- texlive-ocr-latex
- texlive-ocr-latex
- texlive-ocr-latex
- texlive-ocr-latex

