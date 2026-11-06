# Frequently asked questions

<!-- description: Answers to frequent questions about HinterOS: hardware, Steam, apps, updates, profiles and privacy. -->

## What is HinterOS?

HinterOS is an operating system for a computer that connects to a TV. You operate it with a controller. It plays games, runs TV apps and can be a media server. HinterOS is free software, based on NixOS.

## Which computers can run HinterOS?

A 64-bit (x86_64) computer with UEFI firmware, 4 GB of memory and an internal disk of 17.2 GB or more. For more information, refer to [Install](install.md).

## Does HinterOS work with Secure Boot?

No. Turn off Secure Boot before you install. The installer and the boot loader do not have Secure Boot signatures.

## Can I keep Windows or a different operating system on the same disk?

No. The installer erases the disk that you select.

## Can I play Steam games?

Yes. Install Steam from the Store. Each profile signs in to its own Steam account. For more information, refer to [Steam](steam.md).

## Which controllers can I use?

Controllers with a cable, a USB receiver or Bluetooth. The installer cannot pair Bluetooth controllers. Pair them in first-time setup or in Settings. For more information, refer to [Controls](controls.md).

## Can I use a keyboard and a mouse?

Yes. The home screen accepts a keyboard. A mouse and a keyboard work in apps such as Firefox. For more information, refer to [Controls](controls.md).

## Where do apps come from?

Apps come from the HinterOS Store. Each profile installs its own apps. For more information, refer to [Apps and the Store](apps.md).

## Can apps see my files?

Store apps run in a sandbox. Each app sees only its own folder. An app needs your permission to use the Downloads folder. Steam has full access to its profile. For more information, refer to [Privacy and security](privacy.md).

## Does HinterOS update automatically?

No. The box looks for updates, but it does not install them. A person with the admin PIN installs an update. For more information, refer to [Updates](updates.md).

## What if an update causes a problem?

Roll back to the previous version in Settings → Updates. If a new version does not start, the box starts the previous version. For more information, refer to [Updates](updates.md).

## Can more than one person use the box?

Yes. Each person has a profile with its own apps, Steam account and settings. Visitors can use the Guest profile. For more information, refer to [Profiles](profiles.md).

## Can two people play on a split screen?

No. HinterOS does not have split screen.

## What is the admin PIN?

The admin PIN is the PIN of the admin profile. Updates, box settings and changes to other profiles need it. For more information, refer to [Administration](admin.md).

## I forgot a PIN. What do I do?

The administrator can remove the PIN from the console. For more information, refer to [Profiles](profiles.md).

## Does HinterOS collect data about me?

No. HinterOS sends no usage data and no crash reports. Apps connect to their own services. For more information, refer to [Privacy and security](privacy.md).

## Can the box be a media server?

Yes. The box can run a Jellyfin server or a Plex Media Server. For more information, refer to [Media server](server.md).

## Where do I report a problem?

Report problems in the [source repositories](https://justsomeshed.com/JSwartz/HinterOS). Add the logs from `hinteros-save-log` or `hinteros-diagnose`. For more information, refer to [Troubleshooting](troubleshooting.md).
