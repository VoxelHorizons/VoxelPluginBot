# VoxelPluginBot — Suggested Support Replies

## Production Docker image (GHCR / EasyPanel)

When changes reach `main`, [GitHub Actions](https://github.com/VoxelHorizons/VoxelPluginBot/actions/workflows/docker-image.yml) runs the storage tests, builds the bot container, and publishes:

- `ghcr.io/voxelhorizons/voxelpluginbot:latest`
- `ghcr.io/voxelhorizons/voxelpluginbot:sha-<first-12-commit-characters>` (immutable revision tag)

The workflow can also be started manually with **Run workflow**. No extra GitHub secrets or third-party Actions are needed; it uses the built-in `GITHUB_TOKEN` with `packages: write`.

### EasyPanel setup

1. Wait for the **Publish container to GHCR** workflow to succeed on `main`.
2. GHCR packages are private when first published. In the VoxelHorizons organisation's **Packages** page, either make the `voxelpluginbot` package **Public** for an unauthenticated EasyPanel pull, or configure GHCR credentials for a private pull.
3. In EasyPanel create **Project → New Service → App**, then set **Source → Docker Image** to `ghcr.io/voxelhorizons/voxelpluginbot:latest`.
4. In **Environment**, configure `DISCORD_TOKEN=...` with the real bot token, and optionally `DISCORD_TEST_GUILD_ID=<server-id>` if you previously synced slash commands to that guild. The image already defaults to `DATABASE_PATH=/data/replies.sqlite3`.
5. In **Storage**, add a persistent **Volume** mounted inside the container at `/data`. The container runs as UID/GID `10001:10001`; ensure the mount is writable by that user.
6. Set **one replica**, leave domains and ports unconfigured (the Discord gateway requires outbound access only), then **Deploy**. Check the service logs for `VoxelPluginBot ready as ...`.

**Preserving saved responses:** Before switching off your local Windows bot, stop it and back up its `data/replies.sqlite3`. Copy that database into the EasyPanel `/data/replies.sqlite3` volume **before starting the production bot**, with file ownership/writability for UID 10001. If no database is copied, the container starts with an empty reply database. Do **not** commit the SQLite file or your token to GitHub. Avoid running Windows and EasyPanel copies simultaneously under the same token.

The `latest` tag is updated by GitHub Actions on each push to `main`, but EasyPanel still needs to **Deploy** again to pull and run the newest image. A pinned `sha-...` tag can be used for reproducible releases and rollback.

## Support response pack
This pack contains 28 additional quick replies. It **does not** include or overwrite your existing `!!offline`, `!!support`, `!!support furniture`, or `!!support vehicles` replies.

## Files
- `replies.md` — Readable titles and descriptions for review and copying into `/reply create` manually.
- `replies.json` — Editable response data. Each entry uses `keyword`, `title`, `description`, `color`.
- `import_replies.py` — Optional one-time importer. Does **not** modify `bot.py` or `storage.py`, create channels, or use a Discord token. Backs up the existing database before importing and skips all existing replies.

## Import all at once (Windows / Git Bash)

1. **Stop the running bot** with Ctrl+C.
2. Extract this ZIP and **copy `replies.json` and `import_replies.py` into the same directory as your existing `bot.py`**. No existing files need replacing.
3. From Git Bash, `cd` into that bot directory and run the preview first:
   ```bash
   py -3 import_replies.py --guild YOUR_DISCORD_SERVER_ID
   ```
4. If the preview is correct, apply it:
   ```bash
   py -3 import_replies.py --guild YOUR_DISCORD_SERVER_ID --apply
   ```
5. Restart as usual:
   ```bash
   py -3 bot.py
   ```
6. Test `!!logs`, `!!support core`, `!!install furniture`, and `!!pack bedrock` in Discord. They should reply directly to the original message.

The script expects the existing database at `data/replies.sqlite3` relative to your **current bot directory**. If you use a different database path, add `--db path/to/your.sqlite3`. It creates a timestamped `.backup-...` file next to the database before adding replies. It preserves any saved reply whose keyword already exists. You can change the generated text later with `/reply edit`.

**No changes to the bot's Python source code or dependencies are required.**

## Important
- The bot supports **one optional subkey** only: `!!install furniture`, `!!pack bedrock`, etc.
- The file uses Unicode emoji instead of Discord `:shortcodes:`, so the embeds render properly.
- Some instructions are prompts for troubleshooting, not claims of a guaranteed feature or fix. Content is based on the Core and Furniture release READMEs and linked official wiki guides.
- VoxelVehicles stays private; the `!!vehicles` message directs users to wait for an official public sales channel.
