# revision 30530
# category Package
# catalog-ctan /macros/latex/contrib/horoscop
# catalog-date 2013-05-17 13:43:39 +0200
# catalog-license pd
# catalog-version 0.92
Name:		texlive-horoscop
Version:	0.92
Release:	6
Summary:	Generate astrological charts in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/horoscop
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/horoscop.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/horoscop.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/horoscop.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The horoscop package provides a unified interface for
astrological font packages; typesetting with pict2e of standard
wheel charts and some variations, in PostScript- and PDF-
generating TeX engines; and access to external calculation
software (Astrolog and Swiss Ephemeris) for computing object
positions.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/horoscop/horoscop.sty
%doc %{_texmfdistdir}/doc/latex/horoscop/README
%doc %{_texmfdistdir}/doc/latex/horoscop/horoscop.pdf
#- source
%doc %{_texmfdistdir}/source/latex/horoscop/horoscop.dtx
%doc %{_texmfdistdir}/source/latex/horoscop/horoscop.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
