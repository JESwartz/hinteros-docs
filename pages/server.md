# Media server

<!-- description: Run a Jellyfin or Plex media server on the box, and reach it with Tailscale or Cloudflare Tunnel. -->

The box can run these services for the whole household:

- Jellyfin server: a media server for your movies, series and music.
- Plex Media Server: a Plex server for your movies, series and music.
- Tailscale: your own devices can use the servers of the box from anywhere.
- Cloudflare Tunnel: devices in your Cloudflare Zero Trust network can use the servers of the box.

## The Server tab

The Server tab shows each service and its state: Off, Starting, Running, Needs setup or Error. All profiles can see the tab.

Each change on the Server tab needs the [admin PIN](admin.md).

To turn on a service:

1. Select the service on the Server tab.
2. Select Turn on.
3. If the service has terms, read them and accept them.
4. Type the admin PIN.

To turn off a service, open it and select Turn off. The service keeps its data when it is off.

> [!WARNING]
> The Turn off dialog has the option Delete server data. If you select it, HinterOS deletes the libraries, accounts and settings of the service. You cannot undo this. Your media files stay.

## Put media in /srv/media

Each box has the folder `/srv/media` for movies, series and music. Jellyfin and Plex can read this folder. The admin account can write to it.

Copy your media to the box over SSH. First turn on SSH, as [Network](network.md) tells you. Then use `scp` or an SFTP app on your computer:

```
scp -r Movies <admin>@<address>:/srv/media/
```

Replace `<admin>` with the user name of the admin account. Replace `<address>` with the address of the box.

Put each type of media in its own folder, for example `Movies`, `Shows` and `Music`. The folder list on the box does not show hidden folders or links to other folders.

## Jellyfin

When you turn on Jellyfin server, HinterOS sets it up for you. The page shows "Setting up..." until the server is ready.

### Libraries

A library tells Jellyfin where your media is. To add a library:

1. Open Jellyfin server on the Server tab.
2. Select Add library.
3. Select Folder, then choose a folder in `/srv/media`.
4. Type a name.
5. Select the kind: Movies, Shows, Music or Mixed.
6. Select Add, then type the admin PIN.

To remove a library, select it in the list. The media files stay.

### Accounts

HinterOS makes one Jellyfin account for each profile. The account has the name of the profile. The Guest profile does not get an account.

The Jellyfin app on the box signs in with the account of your profile. The app needs the Local network permission for this. Refer to [Apps and the Store](apps.md).

To use Jellyfin on a phone, a computer or another TV, select Show accounts. The page shows the user name and the password of each account.

### Who can connect

These devices can connect to Jellyfin:

- Devices on your home network.
- Your devices on your Tailscale network, when Tailscale is on.
- Devices in your Cloudflare Zero Trust network, when Cloudflare Tunnel is connected.

Devices on the internet cannot connect to Jellyfin. The Address line on the Jellyfin page shows the address for apps on your home network.

### Backups

An update or a rollback can change the Jellyfin version. Before this change, HinterOS stops Jellyfin and makes a copy of the Jellyfin data. If the copy fails, the update stops and nothing changes.

HinterOS keeps one copy. Each new copy replaces the previous copy. The copy is in `/var/lib/hinteros-root/jellyfin-backup`. HinterOS does not restore it for you.

## Plex Media Server

Plex Media Server comes from Plex, not from HinterOS. You must accept the Plex Terms of Service before you turn it on.

After you turn it on, link the server to your Plex account:

1. On a phone or a computer, go to https://plex.tv/claim and sign in. You can also scan the QR code on the Plex page.
2. Plex shows a claim code. Type the code in the Claim code field. The field starts with `claim-`.
3. Select Link, then type the admin PIN.

The page then shows "Linked to a Plex account." Add libraries in the Plex app. Use folders in `/srv/media`.

Plex apps at home can connect to the server. Plex can also give access from outside your home with its own remote access. Plex controls this access, not HinterOS.

## Tailscale

Tailscale puts the box on your private Tailscale network. To sign in:

1. Turn on Tailscale on the Server tab.
2. Select Sign in, then type the admin PIN.
3. Scan the code on the screen with your phone. Then sign in to Tailscale.

> [!NOTE]
> The first person who opens the sign-in address adds the box to their Tailscale network. Do not show the code to other people.

If the page shows "The tailnet admin must approve this box.", approve the box in the Tailscale admin console. The page also shows when the key expires. After that date, select Sign in again.

Your devices on the Tailscale network can use Jellyfin, Plex and SSH, when these are on. Sign out stops this access. Tailscale stays on.

## Cloudflare Tunnel

Cloudflare Tunnel connects the box to your Cloudflare Zero Trust network. Devices with the Cloudflare WARP app in your organisation can then use the servers of the box.

1. In the Zero Trust dashboard, make a tunnel. Copy its token.
2. Turn on Cloudflare Tunnel on the Server tab.
3. Type the token in the Tunnel token field.
4. Select Save token, then type the admin PIN.
5. In the Zero Trust dashboard, add a private network route to the address on the line "Route this address in Zero Trust".

The page shows "Connected." when the tunnel works. The tunnel reaches only the ports of the servers on the box. It does not reach SSH.

To stop the tunnel, select Remove token.
