# Controls

<!-- description: Controller buttons, keyboard keys, the on-screen keyboard, the pointer and Bluetooth pairing in HinterOS. -->

HinterOS uses a controller. A keyboard also operates the home screen. This page uses the Xbox names of the buttons, because the screen uses them too.

## The home screen

The top bar has six tabs:

1. Home: The Continue row, then your apps and your games. Continue shows the apps and games that run, then the apps that you opened since you logged in.

2. Games: Your Steam library. Refer to [Steam](steam.md).

3. Apps: All the apps of your profile. Steam is the first tile.

4. Store: Install and remove apps. Refer to [Apps and the Store](apps.md).

5. Server: Jellyfin, Plex, Tailscale and Cloudflare Tunnel. All profiles see this tab. Each change needs the admin PIN. Refer to [Media server](server.md).

6. Settings: Refer to [Settings](settings.md).

Your profile chip and the clock are at the right end of the tab row. When a task such as an update runs, a progress indicator also shows in the tab row. Select it to see the progress.

## Buttons and keys

| Action | Controller | Keyboard |
|---|---|---|
| Move | D-pad or left stick | Arrow keys |
| Open or select | <kbd>A</kbd> | <kbd>Enter</kbd> |
| Back | <kbd>B</kbd> | <kbd>Esc</kbd> or <kbd>Backspace</kbd> |
| Previous or next tab | <kbd>LB</kbd> or <kbd>RB</kbd> | <kbd>Page Up</kbd> or <kbd>Page Down</kbd> |
| Close a running app (on its tile) | <kbd>Y</kbd> | <kbd>Y</kbd> |
| Open Steam when the Steam banner shows | <kbd>X</kbd> | <kbd>X</kbd> |
| Go to Home | Push and release <kbd>Guide</kbd> | <kbd>Ctrl</kbd> + <kbd>Windows</kbd> + <kbd>D</kbd> |
| Steam menu, in Steam or a Steam game | Hold <kbd>Guide</kbd> for half a second | None |
| Show or hide the on-screen keyboard | Hold <kbd>Guide</kbd> and push <kbd>Y</kbd> | None |
| Move the pointer, in keyboard apps | Right stick | Mouse |
| Left click, in keyboard apps | <kbd>RT</kbd> | Mouse |
| Right click, in keyboard apps | <kbd>LT</kbd> | Mouse |

On the tab row, left and right go around from the last tab to the first tab. Up from the top row of a tab goes to the tab row.

<kbd>B</kbd> goes back one level. From the content of a tab, it goes to the Home tab. On the Home tab, it does nothing.

<kbd>Guide</kbd> always goes to the Home tab and highlights the first tile. An app or a game that has the screen continues to run. Its tile shows in the Continue row.

<kbd>LB</kbd> and <kbd>RB</kbd> change the tab from all places on the home screen, but not in a dialog.

While a text field has the focus, the letter keys and <kbd>Backspace</kbd> type text. <kbd>Esc</kbd> goes back.

Some actions cannot be undone, for example to remove a profile. For these actions, hold <kbd>A</kbd> on the button until it fills with red. Release it early to stop.

To change which button does which action, refer to [Settings](settings.md).

## Start and close apps

1. Highlight a tile and push <kbd>A</kbd>.

2. While the start screen shows, push <kbd>B</kbd> to stop the wait and go back to Home.

To close an app:

1. Push <kbd>Guide</kbd>.

2. Highlight the tile of the app. A running app has a running mark.

3. Push <kbd>Y</kbd>.

4. Select Close. Unsaved work in the app can be lost.

## The profile picker

To change to a different profile, select your profile chip at the right end of the tab row. The chip shows the colour and the initial of your profile.

The picker shows the profiles, Guest and Add profile. To go back to your session, select your own profile or push <kbd>B</kbd>. Refer to [Profiles](profiles.md).

## The on-screen keyboard

The keyboard opens:

- By itself, when a text field on the home screen gets the focus.

- When you push <kbd>A</kbd> on a text field in a keyboard app.

- When you click into a text field with <kbd>RT</kbd> in a keyboard app.

- When you hold <kbd>Guide</kbd> and push <kbd>Y</kbd>. This works in all apps.

| Button | Action |
|---|---|
| D-pad or left stick | Move between the keys |
| <kbd>A</kbd> | Type the key |
| <kbd>B</kbd> | Close the keyboard |
| <kbd>X</kbd> | Delete the last character. Hold to delete more |
| <kbd>Y</kbd> | Shift. Push again for Caps. Push a third time for lower case. On the symbol pages, go to the other symbol page |
| <kbd>LB</kbd> | Letters page |
| <kbd>RB</kbd> | Symbols page |

The keyboard also has the keys ?123 and abc to change the page, and Tab, Space, Backspace, Enter and Done. Done closes the keyboard.

The strip above the keys shows the text that you typed. In a password field, it shows dots. To change this, refer to [Accessibility](accessibility.md). Some characters cannot be typed. The strip then shows a message.

<kbd>Guide</kbd> and a change to a different app also close the keyboard.

## Keyboard apps and the pointer

Web apps such as YouTube, Netflix and Firefox are keyboard apps. Some games are keyboard apps too. In a keyboard app, the controller sends keys:

- The D-pad and the left stick send the arrow keys.

- <kbd>A</kbd> sends <kbd>Enter</kbd>. <kbd>A</kbd> never clicks.

- <kbd>B</kbd> sends <kbd>Esc</kbd>.

The right stick moves a mouse pointer. <kbd>RT</kbd> is the left click and <kbd>LT</kbd> is the right click. To drag, hold the trigger and move the right stick.

The D-pad and the left stick hide the pointer. The right stick and the triggers show it again.

In Firefox, <kbd>View</kbd> selects the address bar and opens the on-screen keyboard. <kbd>LB</kbd> and <kbd>RB</kbd> go back and forward in the history.

To change the pointer speed or the click buttons, refer to [Settings](settings.md).

## Steam and games

Steam and Steam games get the controller directly. The Controller settings of HinterOS do not change them. <kbd>Guide</kbd> still goes to Home.

In Steam or a Steam game, hold <kbd>Guide</kbd> for half a second to open the Steam menu. Over a game, this is the in-game menu of Steam. A shorter push goes to Home. Refer to [Steam](steam.md).

## Mouse and keyboard

The home screen does not use a mouse. Use a controller or the keys in the table. A USB or Bluetooth mouse and keyboard work in apps such as Firefox.

## Pair a Bluetooth controller

1. Go to Settings → Network → Bluetooth.

2. Select Look for new devices. The search stops after 30 seconds.

3. Put the controller in pairing mode.

4. Select the controller in Devices, then select Pair.

Most controllers and headsets pair without a code. Some devices show a code:

- If the screen asks if the device shows the same code, compare the two codes. Then select Accept or Reject.

- If the screen tells you to type a code, type it on the device and push <kbd>Enter</kbd> there.

A paired controller connects again by itself.

To disconnect or remove a device, select it. Then select Disconnect or Forget this device.

The installer cannot pair Bluetooth controllers. Use a controller with a cable or a USB receiver for the installation.

## Power button

Push the power button of the computer to put it to sleep. Hold the power button to shut down the computer.
