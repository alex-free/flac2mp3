Name:           flac2mp3
Version:        1.0
Summary:        Recursively convert a folder of FLAC files to one containing 320kbs stereo MP3 files.
Release:        1%{?dist}
License:        3-BSD
URL:            https://github.com/alex-free/ezreflac2mp3
Packager:       Alex Free

%description
Recursively convert a folder of FLAC files to one containing 320kbs stereo MP3 files.

%install
mkdir -p %{buildroot}/usr/bin
cp %{_sourcedir}/flac2mp3 %{buildroot}/usr/bin/

%files
/usr/bin/flac2mp3
