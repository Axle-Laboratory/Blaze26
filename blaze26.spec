Name:           blaze26
Version:        1.0
Release:        1
Summary:        BlazeOS 26 cinematic shell
License:        MIT
BuildArch:      noarch

%description
Modular launcher and cinematic shell for BlazeOS 26.

%prep
echo "Preparing Blaze26"

%build
echo "Building Blaze26"

%install
install -D -m 755 %{SOURCE0} %{buildroot}/usr/bin/blaze26-launcher
install -D -m 644 %{SOURCE1} %{buildroot}/usr/share/applications/blaze26.desktop
install -D -m 644 %{SOURCE2} %{buildroot}/usr/share/icons/blaze26-logo.png

%files
/usr/bin/blaze26-launcher
/usr/share/applications/blaze26.desktop
/usr/share/icons/blaze26-logo.png
