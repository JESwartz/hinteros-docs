# Administration

<!-- description: The admin account, the admin PIN, forgotten PINs, console login, sudo and SSH on a HinterOS box. -->

A HinterOS box has two kinds of administrator access:

- The admin account: a Linux account for the console and SSH. You make it in the installer.
- The admin profile: the first profile, which you make in first-time setup. Its PIN is the admin PIN.

## The admin account

The installer asks for the admin account in the Admin account step. Type a user name and a password of 8 characters or more.

The admin account is not a profile. It does not show on the TV. Use it for these tasks:

- Log in on the console.
- Log in over SSH.
- Use `sudo`.
- Turn SSH on or off in Settings.

Only the admin account has a password. Profiles and root have no password. They cannot log in on the console or over SSH.

You cannot change the admin password in Settings. To change it, run the installer again with Keep data on, and type a new password. For more about the installer, refer to [Install](install.md).

## The admin PIN

The admin PIN is the PIN of the admin profile. You choose it when you make your profile in first-time setup. It has 4 to 8 digits.

These actions need the admin PIN, from all profiles:

- Install an update, roll back or change the update channel.
- Change the time zone in Settings. First-time setup does not ask for the PIN.
- Clean up the system or the profiles, and change the automatic clean-up.
- Open the storage of a different profile.
- Rename or remove a different profile, or give it a new PIN.
- Turn Guest on or off, and change the starter apps.
- Each change on the Server tab, and Show accounts for Jellyfin.
- Cancel a task that a different profile started.

For more about profiles, refer to [Profiles](profiles.md).

### Change the admin PIN

1. In the admin profile, go to Settings → Profiles.
2. Select your profile, then select Change PIN.
3. Type your current PIN, then the new PIN two times.

### Too many wrong PINs

After 10 wrong admin PINs, the box refuses the admin PIN until it restarts. It also refuses the correct PIN. The screen shows "Too many wrong PINs. Restart the box to try again."

The count includes wrong PINs from all places, such as the profile picker and Settings. A restart of the box sets the count to zero. A correct PIN before the tenth wrong PIN also sets the count to zero.

## Forgotten PINs

You can remove the PIN of any profile from the console or over SSH. Log in as the admin account. To see the profiles and their ids, type:

```
sudo hinteros-system reset-pin
```

To remove the PIN of one profile, add its id or its exact name:

```
sudo hinteros-system reset-pin p2
```

The profile then opens without a PIN. At its next start it asks for a new PIN.

This also works for the admin profile. It also sets the count of wrong admin PINs to zero, so you do not have to restart the box. Until the admin profile has a new PIN, only the admin profile can do the actions that need the admin PIN.

## The console

The console is a text screen on the box.

1. Connect a keyboard to the box.
2. Press <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>F2</kbd>.
3. Log in with the user name and the password of the admin account.

To go back to the TV screen, press <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>F1</kbd>.

## sudo

The admin account can run commands as root with `sudo`. `sudo` asks for the password of the admin account.

> [!WARNING]
> Commands as root can delete data and stop the box from starting. Type only commands that you understand.

## SSH

SSH gives the same access as the console, from a computer on your home network. Only the admin account can log in. To turn on SSH and connect, refer to [Network](network.md).

## Other commands

To show a report about the network and the hardware, type:

```
hinteros-diagnose
```

The report fits on one or two TV screens. To show all lines, add `--full`. For more help, refer to [Troubleshooting](troubleshooting.md).
