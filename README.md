# HinterOS documentation

User documentation for [HinterOS](https://hinteros.org), a controller-driven game console and
TV operating system for living-room computers. The website shows these pages at
https://hinteros.org/docs/.

For development information, refer to the READMEs in the
[source repositories](https://justsomeshed.com/JSwartz/HinterOS).

## Pages

- [Install](pages/install.md)
- [Controls](pages/controls.md)
- [Profiles](pages/profiles.md)
- [Apps and the Store](pages/apps.md)
- [Steam](pages/steam.md)
- [Media server](pages/server.md)
- [Network](pages/network.md)
- [Settings](pages/settings.md)
- [Accessibility](pages/accessibility.md)
- [Updates](pages/updates.md)
- [Administration](pages/admin.md)
- [Privacy and security](pages/privacy.md)
- [Troubleshooting](pages/troubleshooting.md)
- [Frequently asked questions](pages/faq.md)

## Write a page

Each page is `pages/<slug>.md`. `pages.toml` gives the reading order and the line for each page
on the overview. A page starts with its title and a description for search engines:

```markdown
# Install

<!-- description: Install HinterOS and do first-time setup. -->
```

Use only these Markdown parts, so that the page shows correctly here and on the website:

| Part | Write |
|---|---|
| Heading | `##` and `###`. One `#` title for each page |
| List | `-` for items, `1.` for a sequence. Each item is one or more full sentences |
| Emphasis | Do not use bold or italics. Use a heading or a note |
| Link to a page | `[Profiles](profiles.md)` or `[PINs](profiles.md#pins)` |
| Link to the website | `https://hinteros.org/download/` |
| Controller button | `<kbd>A</kbd>`. The website shows these names as controller buttons: A, B, X, Y, LB, RB, LT, RT, Guide, View, Menu |
| Key | `<kbd>Enter</kbd>`. For a key combination: `<kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>F2</kbd>` |
| Menu path | `Settings → System → Apps open at once` |
| Warning | `> [!WARNING]` on the first line of a quotation. Only for loss of data or damage |
| Note | `> [!NOTE]` on the first line of a quotation |
| Command | A code block with no language |
| Steps | `<!-- steps -->` after the description. Then each `##` heading is one step |
| Image | `![Text for screen readers](../images/<name>.png)` |

## Language

Write in ASD-STE100 Simplified Technical English:

- One instruction or one statement in each sentence.
- 20 words or fewer in an instruction. 25 words or fewer in a description.
- Use the imperative for instructions: "Select the disk", not "You should select the disk".
- Use the active voice: "The installer erases the disk", not "The disk is erased".
- Use one word for one thing. Use the names that the screen shows, with the same capitals.
- Do not use "please", "simply", "just" or "easily".
- Tell the reader about a risk before the step that causes it.

Document only what HinterOS does now. Do not document plans.

## Check

```
nix run nixpkgs#python3 -- check.py
```

The check finds pages that are not in `pages.toml` or in this README, broken links between
pages, missing images, missing titles or descriptions, and sentences that are too long.

## License

GPL-3.0-only, like the rest of HinterOS.
