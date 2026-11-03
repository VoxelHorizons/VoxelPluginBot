# VoxelPluginBot — Quick Support Replies

A small Discord support assistant for the existing Voxel Horizons support threads. **No tickets, ticket panels, new channels, or GitHub issue automation.**

Staff with the **Manage Messages** permission can create and edit replies *inside Discord*. Any member can use an existing reply keyword, with a 5-second per-user cooldown.

## Usage

1. Run `/reply create keyword:logsdump` and fill in the popup form with the response text. Titles are optional; replies are green embeds by default. Markdown, links, code formatting and line breaks are supported.
2. Someone types `!!logsdump` in any existing support channel or thread.
3. The bot immediately posts the saved embed in **that same thread/channel**.

To edit later, use `/reply edit keyword:logsdump`. Changes become active immediately—no restart required.

| Staff command | Description |
|---|---|
| `/reply create` | Create a reusable reply in a popup editor |
| `/reply edit` | Edit existing text, title, or embed color |
| `/reply delete` | Remove a reply |
| `/reply list` | List all configured keywords |
| `/reply preview` | Preview a reply privately |

A reply can include `{{user}}`, `{{server}}` or `{{channel}}` placeholders, which expand when invoked. Replies are scoped to the Discord server and stored in SQLite, surviving bot restarts.

## Setup

1. Create a bot at <https://discord.com/developers/applications>. Under **Bot → Privileged Gateway Intents**, enable **Message Content Intent** for triggers such as `!!logsdump`. Discord may require approval for some verified apps.
2. Invite the bot with `bot` and `applications.commands` scopes. Give it **View Channels**, **Send Messages**, **Send Messages in Threads**, **Embed Links** and **Read Message History**. It does **not** need Administrator, Manage Channels, or Manage Roles.
3. Install Python 3.11+ and run `python -m pip install -r requirements.txt`.
4. Set `DISCORD_TOKEN` in the environment. For example, in Git Bash: `export DISCORD_TOKEN='your-token-here'` (do not paste or commit your token anywhere public).
5. Run `python bot.py`.
6. Optionally set `DISCORD_TEST_GUILD_ID` to your test server ID to register slash commands quickly on that server. Without it, commands sync globally and may take time to appear.

The SQLite file defaults to `data/replies.sqlite3`. Store it on persistent disk when hosting. If you lose it, you lose the created replies. Back it up before moving hosts.

## Notes

- Only an exact standalone trigger such as `!!offline` activates a reply; other messages are ignored.
- Staff need **Manage Messages** permission to use `/reply` administration commands; invocations are open to everyone.
- Replies intentionally suppress @mentions to avoid unwanted pings.
- Existing support channels and release announcement webhooks remain unchanged.
- Use the bot for Voxel Horizons support content; example triggers are not preloaded.
