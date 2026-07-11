%global tl_name horoscop
%global tl_revision 56021

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.01
Release:	%{tl_revision}.1
Summary:	Generate astrological charts in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/horoscop
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/horoscop.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/horoscop.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/horoscop.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The horoscop package provides a unified interface for astrological font
packages; typesetting with pict2e of standard wheel charts and some
variations, in PostScript- and PDF-generating TeX engines; and access to
external calculation software (Astrolog and Swiss Ephemeris) for
computing object positions.

