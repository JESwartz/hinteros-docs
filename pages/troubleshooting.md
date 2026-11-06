# Troubleshooting

<!-- description: Fix installer start problems, failed installs, network problems and a box that does not start. Find the logs. -->

## The installer does not start

Do these checks:

- Make sure that Secure Boot is off.

- Make sure that the computer starts the USB stick in UEFI mode. In legacy BIOS mode, the installer refuses to install.

- Write the ISO file to the USB stick again with a tool that writes disk images. Do not use Ventoy.

- Try a different USB stick. A bad USB stick can stop the start.

The installer waits up to five minutes for a slow USB stick. If the message "timed out waiting for /dev/disk/by-label/HINTEROS" shows, the computer cannot read the USB stick.

### Verbose boot

The installer boot menu has a second entry, "(debug: verbose boot)". This entry starts the same installer and shows all the start messages. Use it to see where the start stops. Take a photo of the last messages for your problem report.

## The install does not finish

When the install stops, the screen shows the cause and a Details line.

- "The install did not start": the installer did not change the disk.

- "The install did not finish": the disk can have changes. HinterOS can fail to start.

Select Try again to try the install again. After Erase and install, Try again goes back to the Summary screen. If the disk changed, select Select the disk. If a newer version did not install, select Choose another version and install the version on the USB stick.

If another disk in the computer has an old HinterOS install, the installer refuses to install. Disconnect that disk or erase it.

## Use the console during the install

The installer has a console for problems.

1. Push <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>F2</kbd>. The console opens as the root user.

2. Type your commands.

3. To go back to the installer screens, type `back` or push <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>F1</kbd>.

If the installer screens stop, the console shows on the screen. Type `back` to start the installer screens again. To connect to Wi-Fi from the console, type `nmtui`.

## Network or hardware problems

This command shows a report of the network hardware and connections:

```
hinteros-diagnose
```

The report fits on one or two TV screens. You can take a photo of it. For the full report, add `--full`.

An Ethernet port with the status "unavailable" has no link. Examine the cable first.

On an installed box, log in as the admin and use `sudo hinteros-diagnose`. Without `sudo`, the report does not include the kernel messages.

## Save the installer logs

The installer keeps its logs in memory. Save them before you restart the computer.

1. Connect a second USB stick to the computer. Do not use the installer USB stick.

2. Open the console with <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>F2</kbd>.

3. Type `lsblk` to find the name of the second USB stick, for example `/dev/sdb`.

4. Type this command with the name of the USB stick:

```
hinteros-save-log /dev/sdX
```

The USB stick can use FAT32, exFAT, NTFS or ext4. The command saves the install log, the system log and hardware reports in a new folder on the USB stick. When it shows "Done: it is safe to remove the stick.", remove the USB stick. Attach the files to your problem report.

## The box does not start after an update

HinterOS counts the starts of a new version. If the new version does not start correctly three times, the box starts the previous version.

To select a version yourself, hold <kbd>Space</kbd> on a keyboard while the box starts. The boot menu shows the recent versions. Select an older version.

When the box starts, you can go back to the previous version. Select Settings → Updates → Roll back to the previous version. For more information, refer to [Updates](updates.md).

## Install again and keep your data

If the box does not start, start the installer again. When the disk has a HinterOS install, the Disk screen comes after the Internet screen.

1. On the Disk screen, select Keep data. Erase all erases the disk.

2. Go through the other screens. Keep data has no Apps screen. An empty password keeps the current admin password.

3. On the Summary screen, hold <kbd>A</kbd> on Keep data and install for 5 seconds.

The installer installs HinterOS again and keeps your profiles and files. It always installs the version on the USB stick. If the install on the disk is newer, the Disk screen tells you. For more information about the installer, refer to [Install](install.md).

## Forgotten PIN

The admin can remove the PIN of a profile from the console. Push <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>F2</kbd>, log in as the admin and type this command:

```
sudo hinteros-system reset-pin <name>
```

The profile chooses a new PIN at its next start. Refer to [Profiles](profiles.md).

## Logs

The installer writes its log to `/var/log/hinteros-install.log`. The screen shows this path when the install stops.

On an installed box, log in as the admin. To see the system log of the current start, type this command:

```
sudo journalctl -b
```
