# Network

<!-- description: Connect the box to Wi-Fi or Ethernet, turn SSH on or off, and control which apps can use your home network. -->

The box needs the internet for updates, the Store and some apps, such as Steam.

## Ethernet

Connect a network cable to the box. The box connects automatically. You do not have to set anything.

## Wi-Fi in first-time setup

If you connected to Wi-Fi in the installer, the box keeps that network. It is online when it starts for the first time.

The Internet step of first-time setup shows the networks nearby. To join a network, select it. If the network has a password, type it and select Join.

You can select Continue without a network. The step then shows "Not online. Updates and the Store need the internet." You can connect later in Settings.

## Wi-Fi in Settings

Go to Settings → Network. The top line shows the connection, for example "Connected to Home (192.168.1.42)." The address in brackets is the address of the box on your network.

- To turn Wi-Fi on or off, select Wi-Fi.
- To join a network, select it in Networks nearby. If the network needs a password, type it and select Connect.
- To look for networks again, select Scan again.
- To disconnect or forget a network, select the network that is connected. Then select Disconnect or Forget this network.

Each network in the list shows its state: Connected, Saved, Open, Needs a password or Not supported. The box joins a saved network without a password.

If the saved password of a network changes, the box asks for the new password.

### Networks that do not work

- WEP networks and networks with a business login show "Not supported". The box cannot join them.
- The list does not show hidden networks. You cannot join a hidden network from the screen.

## When the box is offline

The top line in Settings → Network tells you what is wrong:

- "Not connected." The box has no network. Connect a cable or join a Wi-Fi network.
- "No internet." The box has a network, but the network cannot reach the internet. Examine your router.
- "The network needs a sign-in." The network wants you to sign in on a web page, as in a hotel.

When the box cannot reach the update server, Settings → Updates shows "Can't reach the update server right now. Try again later."

For more help, refer to [Troubleshooting](troubleshooting.md).

## Local network permission

Many apps on the box run in a sandbox. An app in a sandbox can use the internet. To use your home network, the app needs the Local network permission.

Without this permission, the app cannot connect to:

- Other devices on your home network, such as a computer, a printer or a media server.
- The servers on the box itself, such as Jellyfin.

For example, the Jellyfin app needs this permission to play from a Jellyfin server at home. You can turn the permission on or off on the page of the app in the Store. The change applies the next time that the app starts. For more about permissions, refer to [Apps and the Store](apps.md).

Apps with full access, such as Steam, can always use your home network.

## SSH

SSH lets you log in to the box from a computer. You log in as the admin account, with its password. For more about the admin account, refer to [Administration](admin.md).

### Turn SSH on or off

You can turn on SSH in the installer, with Enable SSH. To change it later:

1. Go to Settings → System → Remote access.
2. Select SSH.
3. Type the password of the admin account.

After three wrong passwords, nothing changes.

### Connect

On a computer on the same network, type:

```
ssh <admin>@<address>
```

Replace `<admin>` with the user name of the admin account. Replace `<address>` with the address that Settings → Network shows. When SSH is on, Remote access also shows the name of the box on the network. You can try this name in place of the address.

The first time that you connect, `ssh` shows a key fingerprint. Compare it with the SSH host key in Settings → System → About. If they are not the same, do not continue.

### Who can connect

- Only computers on your home network can connect. Computers on the internet cannot.
- When Tailscale is on, your devices on your Tailscale network can also connect. Refer to [Media server](server.md).
- Only the admin account can log in. Profiles and root cannot log in over SSH.
- Each connection gets three tries for the password.
