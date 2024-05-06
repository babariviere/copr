Name:           wayprompt
Version:        0.1.0
Release:        0
Summary:        Multi-purpose prompt tool for Wayland
License:        GPL-3.0-only
URL:            https://git.sr.ht/~leon_plickat/wayprompt

BuildRequires:  git
BuildRequires:  scdoc
BuildRequires:  zig = 0.11.0
BuildRequires:  zig-rpm-macros = 0.11.0
BuildRequires:  zstd
BuildRequires:  pkgconfig(fcft)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wayland-server) >= 1.20.0
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  gcc

Provides:       pinentry-wayprompt = %{version}

%description

%prep
rm -rf * .*
git clone --recurse-submodules --depth 1 %{url} .

%build
%zig_build -Dpie

%install
%zig_install -Dpie

%files
%{_bindir}/%{name}
%{_bindir}/pinentry-%{name}
%{_bindir}/%{name}-ssh-askpass
%license LICENSE
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/pinentry-%{name}.1.gz
%{_mandir}/man1/%{name}-ssh-askpass.1.gz
%{_mandir}/man5/%{name}.5.gz
%doc README.md

%changelog
