Summary:	Lightweight clipboard history
Name:		qlipper
Version:	5.1.1
Release:	1
License:	GPLv2
Group:		Text tools
Url:		https://github.com/pvanek/qlipper
Source0:	https://github.com/pvanek/qlipper/archive/%{version}.tar.gz
BuildRequires:	cmake cmake(ECM) ninja
BuildRequires:	imagemagick

%description
Lightweight and cross-platform clipboard history applet.

%prep
%autosetup -p1
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

install -d -D -m 755 %{buildroot}%{_datadir}/pixmaps
install -d -D -m 755 %{buildroot}%{_iconsdir}

install -D src/icons/%{name}.png %{buildroot}%{_iconsdir}
convert %{buildroot}%{_iconsdir}/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}.*
%{_iconsdir}/*/*/*/%{name}.*
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/%{name}
