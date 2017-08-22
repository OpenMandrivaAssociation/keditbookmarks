Summary:	KDE bookmarks editor
Name:		keditbookmarks
Version:	17.08.0
Release:	1
Epoch:		1
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Test)

%description
KDE bookmarks editor.

%files -f %{name}.lang
%{_kde5_applicationsdir}/org.kde.keditbookmarks.desktop
%{_bindir}/kbookmarkmerger
%{_bindir}/keditbookmarks
%{_datadir}/config.kcfg/keditbookmarks.kcfg
%{_datadir}/kxmlgui5/keditbookmarks
%{_docdir}/HTML/*/keditbookmarks
%{_mandir}/man1/*
%{_mandir}/*/man1/*

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

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

rm -rf %{buildroot}%{_libdir}/libkbookmarkmodel_private.so

%find_lang %{name}
