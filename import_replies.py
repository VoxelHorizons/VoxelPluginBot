#!/usr/bin/env python3
"""Import a curated reply pack into an EXISTING VoxelPluginBot database.

Does not modify existing replies, bot.py, or storage.py.
Python standard library only. Run from the directory containing data/replies.sqlite3.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
import sqlite3
import sys

NAME = re.compile(r"^[a-z0-9_-]{1,32}(?: [a-z0-9_-]{1,32})?$")


def main() -> int:
    parser = argparse.ArgumentParser(description="Preview or import VoxelPluginBot canned replies")
    parser.add_argument("--guild", default=os.environ.get("DISCORD_TEST_GUILD_ID"), help="Discord server (guild) ID; may also use DISCORD_TEST_GUILD_ID")
    parser.add_argument("--db", default=os.environ.get("DATABASE_PATH", "data/replies.sqlite3"), help="Existing bot SQLite database")
    parser.add_argument("--apply", action="store_true", help="Back up database then import new replies; no overwrites")
    args = parser.parse_args()
    if not args.guild or not args.guild.isdecimal() or int(args.guild) <= 0:
        parser.error("provide a numeric --guild YOUR_SERVER_ID (or DISCORD_TEST_GUILD_ID)")
    guild_id = int(args.guild)
    db = Path(args.db).expanduser().resolve()
    if not db.is_file():
        parser.error(f"Bot database not found: {db}. Run from your bot folder; no files were changed.")
    try:
        items = json.loads((Path(__file__).parent / "replies.json").read_text(encoding="utf-8"))
        assert isinstance(items, list)
        for item in items:
            assert set(item) == {"keyword", "title", "description", "color"}
            assert NAME.fullmatch(item["keyword"])
            assert 0 <= len(item["title"]) <= 150
            assert 1 <= len(item["description"]) <= 4000
            assert re.fullmatch(r"[0-9a-fA-F]{6}", item["color"])
        assert len({item["keyword"] for item in items}) == len(items)
    except (OSError, UnicodeError, ValueError, TypeError, AssertionError, KeyError) as exc:
        parser.error(f"Invalid replies.json: {exc}")

    conn = sqlite3.connect(db, timeout=15)
    try:
        exists = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='replies'").fetchone()
        if not exists:
            parser.error(f"Not a VoxelPluginBot database: {db}. No files were changed.")
        current = {row[0] for row in conn.execute("SELECT keyword FROM replies WHERE guild_id=?", (guild_id,))}
        new = [item for item in items if item["keyword"] not in current]
        print(f"Database: {db}\nServer ID: {guild_id}\nAvailable replies in pack: {len(items)}\nAlready present (will preserve): {len(items)-len(new)}\nNew replies: {len(new)}")
        for item in new: print(f"  + !!{item['keyword']}")
        if not args.apply:
            print("\nPREVIEW ONLY. To import, rerun with --apply.")
            return 0
        if not new:
            print("\nNothing to import. Existing replies unchanged.")
            return 0
        stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
        backup = db.with_name(f"{db.name}.backup-{stamp}")
        if backup.exists():
            parser.error(f"Backup path exists: {backup}; no files were changed.")
        # SQLite's backup API creates a consistent copy even if another connection exists.
        with sqlite3.connect(backup) as backup_conn:
            conn.backup(backup_conn)
        print(f"\nBackup created: {backup}")
        with conn:
            conn.executemany(
                "INSERT OR IGNORE INTO replies (guild_id, keyword, title, body, color) VALUES (?, ?, ?, ?, ?)",
                [(guild_id, i["keyword"], i["title"], i["description"], int(i["color"],16)) for i in new],
            )
        print(f"Imported {len(new)} replies. Existing replies were not overwritten.")
        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    sys.exit(main())
