#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE bookmarks editor
Name:		keditbookmarks
Version:	25.08.3
Release:	%{?git:0.%{git}.}1
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/keditbookmarks/-/archive/%{gitbranch}/keditbookmarks-%{gitbranchd}.tar.bz2#/keditbookmarks-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/keditbookmarks-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Test)

%rename plasma6-keditbookmarks

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KDE bookmarks editor.

%files -f %{name}.lang
%{_datadir}/applications/org.kde.keditbookmarks.desktop
%{_datadir}/qlogging-categories6/keditbookmarks.categories
%{_bindir}/kbookmarkmerger
%{_bindir}/keditbookmarks
%{_datadir}/config.kcfg/keditbookmarks.kcfg
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%define kbookmarkmodel_private_major 6
%define libkbookmarkmodel_private %mklibname kbookmarkmodel_private %{kbookmarkmodel_private_major}

%package -n %{libkbookmarkmodel_private}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libkbookmarkmodel_private}
Shared library for %{name}.

%files -n %{libkbookmarkmodel_private}
%{_libdir}/libkbookmarkmodel_private.so.%{kbookmarkmodel_private_major}*
%{_libdir}/libkbookmarkmodel_private.so.5.97.0
