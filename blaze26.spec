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
mkdir -p %{buildroot}/usr/bin
echo "#!/bin/bash\necho BlazeOS 26 launcher" > %{buildroot}/usr/bin/blaze26-launcher
chmod +x %{buildroot}/usr/bin/blaze26-launcher

%files
/usr/bin/blaze26-launcher
