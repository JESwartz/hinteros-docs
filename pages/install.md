# Install

<!-- description: Install HinterOS from a USB stick and do first-time setup. -->

<!-- steps -->

## Check the computer

HinterOS needs:

- A 64-bit (x86_64) processor.

- 4 GB of memory or more.

- UEFI firmware.

- An internal disk of 17.2 GB or more.

A controller with a cable or a USB receiver, or a USB keyboard, operates the installer. The installer cannot pair Bluetooth controllers.

> [!WARNING]
> The installer erases all data on the disk that you select. Make a copy of the data that you want to keep before you install.

## Write the installer to a USB stick

1. Download the ISO file from https://hinteros.org/download/.

2. Compare the checksum of the file with the value on the download page.

3. Write the ISO file to a USB stick with a tool that writes disk images. The USB stick must be larger than the ISO file.

Do not copy the ISO file onto the USB stick as a file. Ventoy is not tested, and the installer can fail to start from it.

## Start from the USB stick

1. Open the firmware settings of the computer.

2. Turn off Secure Boot. The installer and the boot loader do not have Secure Boot signatures.

3. Start the computer from the USB stick in UEFI mode.

4. In the boot menu, select the first entry. Its name is HinterOS, the version number and Installer.

The USB stick also starts in legacy BIOS mode, but the installer then refuses to install. If the installer does not start, refer to [Troubleshooting](troubleshooting.md).

## Go through the installer screens

Use the D-pad to move. Push <kbd>A</kbd> to choose and <kbd>B</kbd> to go back. On a keyboard, use the arrow keys, <kbd>Enter</kbd> and <kbd>Esc</kbd>.

The screens come in this order:

1. Welcome: Select Start.

2. Internet: A network cable connects automatically. To use Wi-Fi, select a network and type its password. To install without a network, select Continue without internet.

3. HinterOS version: This screen shows only when the computer is online and a newer HinterOS is available.

4. Admin account: Type a User name and a Password with 8 or more characters.

5. Options: Set the Computer name, Enable SSH and the Update channel.

6. Apps: Select the first apps.

7. Disk: Select the disk for HinterOS.

8. Summary: Examine all your answers.

The installer keeps the Wi-Fi connection for the installed system.

### Admin account

The admin account is for SSH and for administration commands. HinterOS also asks for this password when you turn on SSH. Keep the password in a safe place. For more information, refer to [Administration](admin.md).

### Options

The default Computer name is hinteros. Enable SSH is off by default. When it is on, other computers on your network can log in as the admin. The Update channel is Stable or Beta.

### Apps

Jellyfin, YouTube and Firefox are on the installer. These apps install without a network. YouTube and Firefox are selected by default.

Steam, VacuumTube and Plex need the internet. Without a network, the installer shows "Needs internet" for these apps. Steam and Plex have vendor terms. Select Read and accept for each of these apps before you continue. You can add more apps later from the Store. Refer to [Apps and the Store](apps.md).

### Online and offline installs

An offline install uses general drivers. HinterOS adds the drivers for your hardware with a later update, when the computer is online.

### Newer version

When the computer is online, the installer looks for a newer HinterOS on the update channel. If it finds one, select the version to install. The version on the USB stick is the default. The newer version needs the internet during the install.

## Hold to install

On the Summary screen, hold <kbd>A</kbd> or <kbd>Enter</kbd> on Erase and install for 5 seconds. A shorter push does nothing. Back changes nothing.

The installer shows each step and a percentage. Do not turn off the computer.

If an app does not install, HinterOS still installs. The last screen shows the names of these apps. Add them later from the Store.

## Restart

1. Remove the USB stick.

2. Select Restart now.

## Do first-time setup

At the first start, HinterOS shows Set up HinterOS. The screens come in this order:

1. Welcome: Select Start.

2. Controllers: Put a Bluetooth controller in pairing mode, then select it. This step is optional.

3. Internet: If a cable is not connected, select a Wi-Fi network. Updates and the Store need the internet.

4. Time zone: Select your time zone.

5. Display: Select a resolution if the display has more than one. Check the picture edges. This step is optional.

6. Create your profile: Type your name, pick a colour and choose a PIN of 4 to 8 digits. Then set Lock this profile and select Create my profile.

7. All set: Select Go to Home.

Your profile is the admin profile. HinterOS asks for its PIN to manage other profiles and the box. For more information, refer to [Profiles](profiles.md).
