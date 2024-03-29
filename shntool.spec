Summary:	Multi-purpose WAV and SHN file processing and reporting utility
Summary(pl.UTF-8):	Wielofunkcyjne narzędzie raportujące i konwertujące pliki WAV i SHN
Name:		shntool
Version:	3.0.10
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://shnutils.freeshell.org/shntool/dist/src/%{name}-%{version}.tar.gz
# Source0-md5:	5d41f8f42c3c15e3145a7a43539c3eae
URL:		http://shnutils.freeshell.org/shntool/
BuildRequires:	autoconf
BuildRequires:	automake
Suggests:	alac_decoder
Suggests:	flac
Suggests:	kexis
Suggests:	shorten
Suggests:	sox
Suggests:	wavpack
# TODO: mp4als, mac (.ape), bonk, la, lpac, ofr, ttaenc (tta)
# mkwcon (.mkw) and takc (.tak) are win32-only
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shntool is a multi-purpose tool for processing and reporting on files
in Shorten and WAVE format. It is can report the size and duration of
WAVE and SHN files, correct files which are not properly
CD-sector-aligned, and stream SHN files to different formats (such as
WAV, FLAC or AIFF).

%description -l pl.UTF-8
Shntool jest wielofunkcyjnym narzędziem do odtwarzania i wyświetlania
raportów o plikach w formacie Shorten i WAVE. Umożliwia wyświetlanie
informacji o rozmiarze i czasie trwania plików WAV i SHN, korygowanie
plików, które nie są prawidłowo wyrównane do wielkości sektora płyty
CD, jak również strumieniową konwersję plików SHN do innych formatów
(takich jak WAV, FLAC lub AIFF).

%prep
%setup -q

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog doc/* README 
%attr(755,root,root) %{_bindir}/shn*
%{_mandir}/man1/shntool.1*
