Name:		texlive-horoscop
Version:	56021
Release:	1
Summary:	Generate astrological charts in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/horoscop
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/horoscop.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/horoscop.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/horoscop.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
