# Privacy and security

<!-- description: What the box sends on the network, and how HinterOS keeps profiles and apps apart. -->

HinterOS sends no usage data and no crash reports. This page tells you what the box connects to, and how HinterOS protects your data.

## What the box connects to

HinterOS itself connects to these servers:

- The HinterOS update server, git.hinteros.org. The box looks for updates when the session starts and one time each day.

- The NixOS package cache, cache.nixos.org. The box downloads updates and apps from it.

- The websites of app vendors. Some apps, for example Plex, download from their vendor during installation. The box also downloads app icons from the vendor websites and gets them again after 30 days.

- The NixOS time servers, nixos.pool.ntp.org. The box sets its clock from them.

The box looks for updates but does not install them. Only a person with the admin PIN can install an update. For more information, refer to [Updates](updates.md).

Apps connect to their own services, for example Steam, Netflix or YouTube. The terms and the privacy rules of the vendor apply.

The media server services run only after the admin profile turns them on. For more information, refer to [Media server](server.md).

### Web apps

Many TV apps, for example YouTube and Netflix, run in Firefox. HinterOS sets Firefox for privacy:

- Firefox telemetry and Firefox studies are off.

- Firefox does not offer to save passwords.

- Firefox installs no add-ons, other than the HinterOS on-screen keyboard.

Some video services need a DRM module. Firefox downloads this module the first time that a service needs it.

## Signed updates

The HinterOS developers sign each update. Before the box installs an update, it checks the signature. The box refuses an update without a correct signature.

The box also refuses a version that is older than a version that it already saw. Thus, a server cannot send an old version with a known security problem.

## Profiles

Each profile is a separate user account on the box. A profile cannot read the files of a different profile.

Each profile has a PIN. After 3 incorrect PINs, HinterOS makes you wait before the next try. Each wait is longer, up to 5 minutes.

The admin PIN has no wait. Instead, after 10 incorrect admin PINs, the box refuses all admin PINs until it restarts. This includes the correct PIN.

> [!NOTE]
> A PIN stops other persons from using a profile by mistake. A person with access to the box can get around it.

For more information, refer to [Profiles](profiles.md) and [Administration](admin.md).

## The app sandbox

Store apps run in a sandbox. Each app has its own folder and cannot see your other files or the files of other apps. An app cannot control HinterOS or other apps.

A filter blocks system functions that apps do not need. If the sandbox or the filter cannot start, HinterOS does not start the app.

An app can use the internet. It needs a permission to use the controller, the microphone, the Downloads folder or the local network.

Without the Local network permission, an app cannot connect to devices on your home network or to services on this box.

Steam cannot run in the sandbox. The Store shows it with the permission Full profile access. For more information, refer to [Apps and the Store](apps.md).

## Display isolation

Each app runs on its own display. An app cannot see the screen of a different app. It also cannot type into a different app, into HinterOS or into the on-screen keyboard.

Steam and Steam games share one display. They do not get a display of their own.

## SSH

SSH is off by default. To turn it on, select Enable SSH in the installer or go to Settings → System → Remote access. You must type the admin password.

When SSH is on, only devices on your local network can connect. The root account cannot log in through SSH. For more information, refer to [Network](network.md).
