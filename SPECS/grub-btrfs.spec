%global debug_package %{nil}
%global _default_patch_fuzz 1
Name:           grub-btrfs
Version:        4.13
Release:	0
Summary:	Automatically add snapshots to your grub entry
License:	GPLv3
URL:		https://github.com/Antynea/grub-btrfs
Source:		https://github.com/Antynea/%{name}/archive/refs/tags/%{version}.tar.gz
Patch0: 0000-add-luks-support.patch
Patch1: 0001-remove-root-requirement.patch
Prefix:		%{_prefix}
Packager:	Samuel Coles
BuildRoot:	%{_tmppath}/%{name}-root

%description
A utility to update grub with btrfs snapshots for easy rollback.

%prep

%setup %{name}-%{version} 
%patch -P 0 -p1
%patch -P 1 -p1

%install

make DESTDIR=%{buildroot} GRUB_UPDATE_EXCLUE=true SYSTEMD=true install

%clean
rm -rf %{buildroot}

%files
/etc/grub.d/41_snapshots-btrfs
/etc/default/grub-btrfs/config
%{_prefix}/bin/grub-btrfsd
%{_prefix}/lib/systemd/system/grub-btrfsd.service
%{_datadir}/licenses/grub-btrfs/LICENSE
%{_datadir}/doc/grub-btrfs/*
%{_prefix}/share/man/man8/grub-btrfs.8.gz
%{_prefix}/share/man/man8/grub-btrfsd.8.gz
