%global qmake_5 /usr/bin/qmake-qt5
%global debug_package %{nil}


Name:		animationmaker
Summary:	Create animated presentations and export them to a video or xml file
License:	GPLv3
URL:		https://github.com/athomasm/delaycut
Version:	1.7
Release:	1%{dist}
Group:		Applications/Multimedia
Source0:	https://github.com/Artanidos/AnimationMaker/archive/v%{version}.tar.gz
Patch:		libpath.patch
Patch1:		desktop_fix.patch
BuildRequires:	qt5-devel 
Recommends:	xdg-utils

%description
AnimationMaker is a software designed to help you to quickly build presentation
video which you can upload to youtube or vimeo. These presentation videos 
can be used as pitch videos for crowdfunding campains for example. 
It is also possible to create animated gifs and HTML animations. The idea for 
the AnimationMaker comes from Adobe Edge which is not available anymore.

%prep
%setup -n AnimationMaker-%{version} 
%ifarch x86_64 
%patch -p1
%endif
%patch1 -p1

%build
%{qmake_5} -makefile AnimationMaker.pro

make

%install

mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}/plugins/gsap
mkdir -p %{buildroot}/usr/share/applications
mkdir -p %{buildroot}/usr/share/icons/hicolor

# App
cp AnimationMaker %{buildroot}/usr/bin
#cp binaries/* %{buildroot}/usr/bin
# Lib
cp Widgets/libWidgets.so* %{buildroot}/%{_libdir}/
# Plugins
cp plugins/Pie/libPie.so %{buildroot}/%{_libdir}/plugins/
cp plugins/Html/libHtml.so %{buildroot}/%{_libdir}/plugins/
cp plugins/Html/gsap/* %{buildroot}/%{_libdir}/plugins/gsap/

# Desktop, #Icon
cp default.desktop %{buildroot}/usr/share/applications
cp default.svg %{buildroot}/usr/share/icons/hicolor


%files
%{_bindir}/AnimationMaker
%{_libdir}/libWidgets.so
%{_libdir}/libWidgets.so.1
%{_libdir}/libWidgets.so.1.0
%{_libdir}/libWidgets.so.1.0.0
%{_libdir}/plugins/gsap/AttrPlugin.min.js
%{_libdir}/plugins/gsap/CSSPlugin.min.js
%{_libdir}/plugins/gsap/EasePack.min.js
%{_libdir}/plugins/gsap/TimelineLite.min.js
%{_libdir}/plugins/gsap/TweenLite.min.js
%{_libdir}/plugins/libHtml.so
%{_libdir}/plugins/libPie.so
%{_datadir}/applications/default.desktop
%{_datadir}/icons/hicolor/default.svg


%changelog

* Wed Jul 18 2018 David Va <davidva AT tuta DOT io> 1.7-1
- Initial build
