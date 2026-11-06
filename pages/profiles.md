# Profiles

<!-- description: Add, change and remove profiles, use PINs, and use the Guest profile. -->

Each person in the household can have a profile. A profile has its own apps, Steam account, sign-ins, settings and files. A profile cannot read the files of a different profile.

The box can have 8 profiles. Only one profile is on the screen at a time.

## The admin profile

The first profile that you make after installation is the admin profile. Its PIN is the admin PIN. The admin PIN is necessary to manage other profiles and the box. You cannot remove the admin profile.

After 10 incorrect admin PINs, the box refuses all admin PINs until it restarts. This includes the correct PIN. For more about the admin PIN, refer to [Administration](admin.md).

## Add a profile

You do not need the admin PIN to add a profile.

1. In the profile picker, select Add profile. In a profile, you can also go to Settings → Profiles → Add profile.

2. Select Choose a name. Type a name of 1 to 32 characters.

3. Pick a colour and select Continue. The profile shows as a circle with this colour and the first letter of the name.

4. Type a PIN of 4 to 8 digits. Then type the same PIN again.

5. Set Lock this profile on or off. Then select Create profile.

HinterOS needs approximately one minute to make the profile. The new profile starts with the starter apps that the admin profile selected.

## PINs

Each profile has a PIN of 4 to 8 digits. You must type your PIN to change the PIN, to lock or unlock the profile, and to remove it.

> [!NOTE]
> A PIN stops other persons from using your profile by mistake. A person with access to the box can get around it.

### Lock a profile

A locked profile asks for its PIN when it opens and after sleep. An unlocked profile opens without the PIN.

1. Go to Settings → Profiles and select your profile.

2. Select Lock this profile or Unlock this profile.

3. Type your PIN.

### Change your PIN

1. Go to Settings → Profiles and select your profile.

2. Select Change PIN.

3. Type your current PIN. Then type the new PIN two times.

### Incorrect PINs

After 3 incorrect PINs for a profile, HinterOS makes you wait before the next try. Each wait is longer than the last one, up to 5 minutes. The screen shows the time to wait.

### Forgotten PIN

If you forget the PIN of a profile, the admin profile can give it a new PIN:

1. In the admin profile, go to Settings → Profiles and select the profile.

2. Select Give it a new PIN. Type the new PIN two times.

3. Type the admin PIN.

If you forget the admin PIN, the administrator must remove it from the console or through SSH. This command shows the profiles and their IDs:

```
sudo hinteros-system reset-pin
```

This command removes the PIN of one profile. Use the ID or the exact name of the profile:

```
sudo hinteros-system reset-pin <ID or name>
```

The profile then opens without a PIN, and HinterOS asks for a new PIN. The command works for all profiles. For the console and SSH, refer to [Administration](admin.md).

## Change profile

> [!WARNING]
> HinterOS closes all apps, games and Steam of the current profile before it opens a different profile. Unsaved progress is lost.

1. Select the profile circle at the top of the screen, next to the clock. The profile picker opens.

2. Select a profile or Guest. To stay in your profile, select your profile or push <kbd>B</kbd>.

3. If a game runs, HinterOS asks first. Select Close it and switch to continue.

4. If the profile is locked, type its PIN.

You can also go to Settings → Profiles, select a profile and select Switch to this profile.

If an app does not close, HinterOS asks what to do:

- Keep waiting: HinterOS waits for the app.

- Force close: HinterOS stops the app. The app can lose unsaved data.

- Cancel switch: Your profile stays open.

## Rename a profile or change its colour

1. Go to Settings → Profiles and select a profile.

2. Select Rename or Colour.

You can change the colour only for your own profile. To rename a different profile, you must type the admin PIN.

## Remove a profile

> [!WARNING]
> When you remove a profile, HinterOS deletes its games, the game saves that are not in the cloud, and all its sign-ins.

1. Go to Settings → Profiles and select the profile.

2. Select Remove. Then select Remove again.

3. For your own profile, type your PIN. For a different profile, type the admin PIN.

4. Hold <kbd>A</kbd> on Delete for 3 seconds.

When you remove your own profile, your session ends first.

## Guest

Guest is a profile for visitors. It starts with the starter apps. HinterOS removes everything in Guest when the guest session ends or the box restarts.

To turn Guest on or off, go to Settings → Profiles → Guest in the admin profile. You must type the admin PIN.

To end the guest session, go to Settings → Profiles → End guest session. HinterOS removes the sign-ins, apps and files of the guest immediately. In Guest, Settings → Profiles shows only Switch profile and End guest session.

## Starter apps

New profiles and Guest start with the starter apps. To select them, go to Settings → Profiles → Starter apps in the admin profile. Then type the admin PIN. Existing profiles do not change.
