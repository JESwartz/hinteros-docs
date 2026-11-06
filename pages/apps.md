# Apps and the Store

<!-- description: Install, remove and update apps, set app permissions, and learn how the sandbox keeps apps apart. -->

Apps come from the Store. Each profile has its own apps. When you install an app, other profiles do not get it.

## The Store

Select Store at the top of the screen. The Store shows the apps in groups: Installed, All, Video, Games, Music, Utilities, Photos and Other.

Select an app to open its page. The page shows the status, the size, the permissions, a description and the vendor terms of the app.

The list of apps comes with HinterOS. A HinterOS update can add apps to the list. When an update has new apps, the Store shows More apps come with the next update.

## Install an app

1. In the Store, select the app. Then select Install.

2. Read the size and the list of other apps that the app needs. If the dialog shows Needs an internet connection, connect the box to the internet.

3. Turn off the optional permissions that you do not want to give. You cannot turn off a required permission.

4. Select Accept, Continue or Install.

5. If the app has vendor terms, read them. Select Accept and install.

The screen shows the progress of the installation. The app then shows in Apps and on Home.

Some apps need a service on the box, for example a media server. Only the admin profile can install a service, in Server. For more information, refer to [Media server](server.md).

Some apps cannot be on the box together. The app page then tells you which app to remove first.

## Update apps

Apps update when HinterOS updates. There is no separate update for each app. For more information, refer to [Updates](updates.md).

You can put the apps of your profile back to an earlier state:

1. Go to Settings → Profiles and select your profile.

2. Select App history. Then select an earlier state.

3. Select Put them back. Your app data stays.

## Remove an app

1. In the Store, select the app. Then select Remove. If the app is open, HinterOS closes it first.

2. To delete the data of the app too, select Also delete this app's data. HinterOS then asks a second time.

3. Select Remove.

> [!WARNING]
> If you delete the data of Steam, HinterOS also deletes all games that this profile installed through Steam.

If you keep the data, the app page shows Removed. Its data stays on the box. To delete the data later, open the app page and select Clear user data.

## App data

Each app in the sandbox keeps its files in its own folder in your profile. Other apps cannot see these files.

To delete the sign-ins, settings and saved files of an app, select Clear user data on the app page. You cannot undo this. When you remove a profile, HinterOS deletes the data of all its apps.

To stop an app that does not respond, select Force stop on the app page. The app stops immediately, and unsaved changes are lost.

## Permissions

Each app in the sandbox can use the internet. An app can use these items only with a permission:

- Controller: The app reads the controller directly.

- Microphone: The app can record sound. Without this permission, the app can only play sound.

- Downloads folder: The app can read and write files in the Downloads folder of your profile.

- Local network: The app can connect to devices on your home network and to services on this box. Without this permission, the app can connect only to the internet.

The app page shows each permission as Required or Optional. To change an optional permission, open the app page and select the permission. The change applies when the app starts again.

## The sandbox

Store apps run in a sandbox. An app in the sandbox:

- Sees only its own folder, and the Downloads folder if it has the permission.

- Cannot see your other files or the files of other apps.

- Cannot control HinterOS or other apps.

- Cannot use the controller, the microphone or the local network without the permission.

## Apps with full access

Some apps cannot run in the sandbox, for example Steam. The Store shows these apps with the permission Full profile access. Such an app can use all data and devices of your profile.

## Vendor terms

Some apps have terms from their vendor, for example Steam, Plex and Modrinth. You must accept the terms before HinterOS installs the app. To read the terms again, open the app page and select Read under Terms.

A starter app with vendor terms shows its terms the first time that you open it. Select Accept and open. If you do not accept the terms, the app stays installed but does not open.

## Apps open at once

Each app runs on its own display. Thus, an app cannot read or type into a different app or into HinterOS.

Settings → System → Apps open at once sets the maximum number of open apps for your profile. You can select 1 to 8 apps. The default is 4. Steam and Steam games do not count.

When all are in use and you open one more app, HinterOS asks which app to close.

> [!NOTE]
> A new value applies after a session restart. When you select Restart session, all open apps close.
