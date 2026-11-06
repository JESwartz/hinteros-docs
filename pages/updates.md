# Updates

<!-- description: Check for HinterOS updates, install them, change the update channel and roll back to an earlier version. -->

HinterOS updates come from the HinterOS update server. The box never installs an update by itself. A person must start each update.

## Channels

Each box follows one channel:

- Stable: the tested releases.
- Beta: the next releases, before they go to Stable.

You choose the channel in the installer, with Update channel. To change the channel later:

1. Go to Settings → Updates.
2. Select Channel, then select the new channel.
3. The box checks the newest version on that channel. It shows the version and its date.
4. Select Switch, then type the admin PIN.

If the version on the new channel is older than the version on the box, the box tells you before you switch.

## Checks for updates

The box checks for updates by itself:

- When the session starts.
- Again each day that the session continues.
- Again when the network comes back after a check failed.

To check now, go to Settings → Updates and select Check for updates.

When an update is available, Home shows a line such as "HinterOS 1.0.1 is available." Select See update to open Settings → Updates.

### Security updates

A security update fixes a security problem. For a security update, the box shows a full screen with the severity. It shows this screen when the session starts and each time that you go back to Home. You can select Later after 5 seconds.

## Install an update

1. Go to Settings → Updates.
2. Select Update now.
3. Read the message. If the update removes apps that you use, the message tells you.
4. Select Update now, then type the admin PIN.

The update needs the admin PIN from all profiles, also from Guest. For more about the admin PIN, refer to [Administration](admin.md).

The box shows the progress of the update. You can cancel the update until it shows "Switching over". The box needs 4 GiB of free disk space for an update.

If the update fails, nothing changes on the box.

## Signed updates

The box installs only an update that has a signature from a HinterOS release key. The version that runs on the box tells which keys it trusts.

The box also refuses these updates:

- A version that does not come after the version on the box.
- A version that is older than a version that the box saw before on that channel.

If an update does not pass these checks, Settings → Updates shows "The update failed its safety check. Nothing was changed." The box keeps the version that it has.

## Restart the session

Some updates change the session itself. When such an update is done, the box shows "The session restarts in 30 seconds." Open games and apps close when the session restarts.

- To restart now, select Restart session.
- To keep playing, select Later. Restart the box later to use the change.

The countdown runs only while the HinterOS screen is in front. It stops while a game or an app is open.

## Roll back

Each update makes a new version of the system. Each change to the box, such as SSH or a server, also makes a new version. Each version has its own copy of the box settings.

> [!NOTE]
> A rollback keeps the time zone that you set.

To go back to the previous version:

1. Go to Settings → Updates.
2. Select Roll back to the previous version.
3. Select Roll back, then type the admin PIN.

To go back to a different version, select it in Versions on this box. The list shows the versions that the box can start. "Current" is the version that runs. "Started with" is the version that the box started with.

A rollback restarts the session. Your apps and games stay. A profile that you made after that version disappears until you update again. Its files stay on the box.

## Automatic fallback

When the box starts a new version, the HinterOS screen must come up in 2 minutes. It must then run for 20 seconds without a problem. If this does not occur, restart the box. The box then tries the new version again.

After 3 failed starts, the box starts the previous version that worked.

To choose a version yourself, hold <kbd>Space</kbd> on a keyboard while the box starts. The boot menu then shows the versions.
