# Settings

<!-- description: The Settings groups of HinterOS: storage, clean-up, display, sound, screen saver, controller and system settings. -->

Settings is the last tab of the home screen. The groups are on the left. The settings of the highlighted group are on the right.

To go into a group, push <kbd>A</kbd> or push right. To go back to the list of groups, push <kbd>B</kbd> or push left. A group with more than one setting shows them one below the other.

Settings has eight groups, in this order: Profiles, Updates, Storage, Network, Display and sound, Accessibility, Controller and System.

Some settings change the whole box. If the admin profile has a PIN, these settings ask for it.

## Profiles

Add, change and remove profiles, set PINs and control the Guest profile. Refer to [Profiles](profiles.md).

## Updates

Check for updates, change the update channel and roll back to an earlier version. Refer to [Updates](updates.md).

## Storage

Storage shows the disk use as a ring. The parts are System, Apps, each profile, Guest, Media, Other and Free space. A profile includes its Steam games. The values come from the last scan.

- To select a part of the ring, push left or right.

- To open a part, push <kbd>A</kbd>. You can open your own profile. A different profile or Guest needs the admin PIN.

- To go one level back out, push <kbd>B</kbd>.

The other items:

- Scan now: Measures the disk again. The row shows the time of the last scan.

- Clean up the system: Removes old versions of HinterOS.

- Clean up profiles: Removes old versions of the apps of each profile.

- Automatic clean-up: Cleans up on a schedule.

### Clean up now

1. Select Clean up the system or Clean up profiles.

2. Push left or right to set Versions to keep, from 1 to 10. The dialog shows the space that the clean-up makes free.

3. Select Clean up and type the admin PIN.

When the clean-up is done, a new scan starts.

> [!NOTE]
> With 1 version to keep, no older version stays. Then you cannot roll back the system, or profiles cannot roll back their apps.

### Automatic clean-up

| Setting | Values | Default |
|---|---|---|
| Clean up automatically | On or off | On |
| How often | Every day, Every week or Every month | Every week |
| System versions to keep | 1 to 10 | 5 |
| App versions to keep | 1 to 10 | 5 |

To save a change, select Save and type the admin PIN.

## Network

Network has two settings: Network and Bluetooth. Refer to [Network](network.md) for Wi-Fi. To pair a controller, refer to [Controls](controls.md).

## Display and sound

### Display

Check the picture edges opens the Safe area screen. The red line must show on all four sides. If the line is cut off, set the TV picture size to "Just scan", "Screen fit" or "1:1".

Resolution and refresh rate shows the modes of the display. When you select a different mode, the screen asks: Keep, or Go back. If you do not answer in 15 seconds, the old mode comes back.

Some displays, for example the internal screen of a laptop, do not let HinterOS change the resolution.

### Audio

- Volume: Push left or right to change the volume in steps of 5%. Push <kbd>A</kbd> to mute or unmute.

- Play sound through: Select the device that plays the sound.

By default, sound plays on the TV through HDMI or DisplayPort, when the display has sound. A device that you select stays selected.

### Screen saver

The screen saver shows only over the home screen. It does not start over an app or a game, for example a film or a paused game. The first button push only closes the screen saver.

| Setting | Values | Default |
|---|---|---|
| Start after | Off, 1 minute, 5 minutes, 10 minutes, 15 minutes or 30 minutes | 10 minutes |
| Style | Clock, Drifting logo or Black screen | Clock |

Show now starts the screen saver at once.

## Accessibility

Text size, High contrast, Focus marker, Reduce motion and Show typed passwords. Refer to [Accessibility](accessibility.md).

## Controller

The Controller settings are for your profile. Changes apply at once. Each setting has Reset to defaults.

### Buttons

Buttons shows one row for each action: Accept, Back, Context, Secondary, Menu, View, Page left, Page right, Left trigger and Right trigger. By default, Accept is <kbd>A</kbd>, Back is <kbd>B</kbd>, Context is <kbd>Y</kbd> and Secondary is <kbd>X</kbd>.

To change a button:

1. Select the action.

2. When the screen shows Press a button, push the new button.

The action that had that button before gets the old button. If you push <kbd>Guide</kbd> or wait 10 seconds, nothing changes.

You cannot change <kbd>Guide</kbd>, the D-pad or the left stick. The new buttons apply on the home screen, in keyboard apps and on the on-screen keyboard. To open the on-screen keyboard, hold <kbd>Guide</kbd> and push the button of Context. Steam and Steam games are not affected.

### Pointer

These settings are for the pointer in keyboard apps:

- Speed: Push left or right to change the speed, from 25% to 400%. The default is 100%.

- Swap sticks: The left stick moves the pointer. The right stick moves like the D-pad.

- Left click: The default is <kbd>RT</kbd>. Select it and push a different button to change it.

- Right click: The default is <kbd>LT</kbd>. If you set the same button as the other click, the two clicks change places.

### Keyboard apps

Keyboard apps sets the key that each button sends in all keyboard apps. Select a row, then select a key or None. By default, the D-pad sends the arrow keys, Accept sends <kbd>Enter</kbd> and Back sends <kbd>Esc</kbd>.

### App keys

App keys lists each keyboard app. Select an app to set keys for only that app. Changed shows next to an app that has its own keys.

## System

### Time zone

Select the time zone of the box. This needs the admin PIN.

### Power

Sleep, Restart and Shut down. Restart and Shut down ask first, because all running apps close.

### Apps open at once

Set how many apps can run at the same time, from 1 app to 8 apps. The default is 4 apps. Steam and Steam games are not included in this number. This setting is for your profile.

A change applies after a session restart. The screen asks Restart the session now? Select Restart, or select Later. All running apps close.

When all places are in use, HinterOS asks you to close an app before it opens the next one.

### Remote access

SSH turns on remote login. To change it, type the admin password. When SSH is on, the screen shows the IP address of the box. Log in at that address as the admin account. Refer to [Administration](admin.md).

### About

About shows the Version, Channel, Software base, Revision, Generation, Host name, IP address and the SSH host key.
