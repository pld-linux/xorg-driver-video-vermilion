Summary:	X.org video driver for Intel Vermilion Range chipsets
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów graficznych Intel Vermilion
Name:		xorg-driver-video-vermilion
Version:	1.0.1
Release:	9
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vermilion-%{version}.tar.bz2
# Source0-md5:	0f7c6be1bbdc5eb43d82b356fe0f5104
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.3.99.0
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-server >= 1.3.99.0
Provides:	xorg-driver-video
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Intel Vermilion graphics chipsets. It can drive
most VERMILION-compatible video cards, but only makes use of the basic
standard VERMILION core that is common to these cards. The driver
supports depths 15 and 24.

%description -l pl.UTF-8
Sterownik obrazu X.org dla układów graficznych Intel Vermilion.
Potrafi obsłużyć większość kart kompatybilnych z VERMILION, ale
wykorzystuje tylko podstawowy standardowy rdzeń VERMILION wspólny dla
tych kart. Sterownik obsługuje głębie kolorów 15 i 24.

%prep
%setup -q -n xf86-video-vermilion-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/*.so
%{_mandir}/man4/vermilion.4*
