Summary:	Multi-purpose WAV and SHN file processing and reporting utility.
Summary(pl):	Wielofunkcyjne narzêdzie raportuj±ce i konwertuj±ce pliki WAV i SHN.
Name:		shntool
Version:	1.2.3
Release:	1
Vendor:		Jason Jordan <shnutils@freeshell.org>
License:	GPL
Group:		Applications/Sound
Source0:	http://shnutils.freeshell.org/shntool/source/%{name}-%{version}.tar.gz
# Source0-md5:	3efbb71b94f5e285daecfe137114873d
Patch0:		%{name}-DESTDIR.patch
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	shorten
Requires:	flac
Requires:	sox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shntool is a multi-purpose tool for processing and reporting on files
in Shorten and WAVE format. It is can report the size and duration of
WAVE and SHN files, correct files which are not properly
CD-sector-aligned, and stream SHN files to different formats (such as
WAV, FLAC or AIFF).


%description -l pl
Shntool jest wielofunkcyjnym narzêdziem do odtwarzania i wy¶wietlania
raportów o plikach w formacie Shorten i WAVE. Umo¿liwia wy¶wietlanie
informacji o rozmiarze i czasie trwania plików WAV i SHN, korygowanie
plików, które nie s± prawid³owo wyrównane do wielko¶ci sektora p³yty
CD, jak równie¿ strumieniow± konwersjê plików SHN do innych formatów
(takich jak WAV, FLAC lub AIFF).


%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog doc/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
