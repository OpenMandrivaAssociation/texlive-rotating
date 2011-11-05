# revision 16832
# category Package
# catalog-ctan /macros/latex/contrib/rotating
# catalog-date 2010-01-26 14:36:34 +0100
# catalog-license lppl
# catalog-version 2.16b
Name:		texlive-rotating
Version:	2.16b
Release:	1
Summary:	Rotation tools, including rotated full-page floats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rotating
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rotating.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rotating.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rotating.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A package built on the standard LaTeX graphics package to
perform all the different sorts of rotation one might like,
including complete figures and tables with their captions. If
you want continuous text (i.e., more than one page) set in
landscape mode, use the lscape package instead. The rotating
packages only deals in rotated boxes (or floats, which are
themselves boxes), and boxes always stay on one page. If you
need to use the facilities of the float in the same document,
load rotating.sty via rotfloat, which smooths the path between
the rotating and float packages.

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
%{_texmfdistdir}/tex/latex/rotating/rotating.sty
%doc %{_texmfdistdir}/doc/latex/rotating/README
%doc %{_texmfdistdir}/doc/latex/rotating/cat.eps
%doc %{_texmfdistdir}/doc/latex/rotating/examples.tex
%doc %{_texmfdistdir}/doc/latex/rotating/rotating.pdf
#- source
%doc %{_texmfdistdir}/source/latex/rotating/rotating.dtx
%doc %{_texmfdistdir}/source/latex/rotating/rotating.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
