# VoxelPluginBot — Suggested Support Replies

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
