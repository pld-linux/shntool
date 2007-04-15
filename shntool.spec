Summary:	Multi-purpose WAV and SHN file processing and reporting utility
Summary(pl.UTF-8):	Wielofunkcyjne narzędzie raportujące i konwertujące pliki WAV i SHN
Name:		shntool
Version:	3.0.2
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://www.etree.org/shnutils/shntool/dist/src/%{name}-%{version}.tar.gz
# Source0-md5:	1b3137a383b43a33191c42d6ecf88bb3
URL:		http://www.etree.org/shnutils/shntool/
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	flac
Requires:	shorten
Requires:	sox
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
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
