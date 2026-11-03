"""Small persistent store for guild-scoped canned Discord support replies."""
from __future__ import annotations

import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path

NAME = re.compile(r"^[a-z0-9_-]{1,32}$")
TRIGGER = re.compile(r"^!!([a-z0-9_-]{1,32})$", re.IGNORECASE)
DEFAULT_COLOR = 0x57F287


@dataclass(frozen=True)
class Reply:
    guild_id: int
    keyword: str
    title: str
    body: str
    color: int


def normalize_keyword(value: str) -> str:
    keyword = value.strip().lower().removeprefix("!!")
    if not NAME.fullmatch(keyword):
        raise ValueError("Use 1–32 letters, numbers, hyphens or underscores.")
    return keyword


def match_trigger(message: str) -> str | None:
    found = TRIGGER.fullmatch(message.strip())
    return found.group(1).lower() if found else None


def parse_color(value: str) -> int:
    value = value.strip().removeprefix("#")
    if not re.fullmatch(r"[0-9a-fA-F]{6}", value):
        raise ValueError("Colour must be six hexadecimal digits, e.g. 57F287.")
    return int(value, 16)


class ReplyStore:
    def __init__(self, path: str | Path):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute(
            """CREATE TABLE IF NOT EXISTS replies (
                   guild_id INTEGER NOT NULL,
                   keyword TEXT NOT NULL,
                   title TEXT NOT NULL DEFAULT '',
                   body TEXT NOT NULL,
                   color INTEGER NOT NULL DEFAULT 5763719,
                   PRIMARY KEY (guild_id, keyword)
               )"""
        )
        self.conn.commit()

    def get(self, guild_id: int, keyword: str) -> Reply | None:
        row = self.conn.execute(
            "SELECT guild_id, keyword, title, body, color FROM replies "
            "WHERE guild_id = ? AND keyword = ?", (guild_id, normalize_keyword(keyword))
        ).fetchone()
        return Reply(**dict(row)) if row else None

    def save(self, guild_id: int, keyword: str, title: str, body: str, color: int) -> None:
        keyword = normalize_keyword(keyword)
        title = title.strip()
        body = body.strip()
        if len(title) > 150 or not body or len(body) > 4000:
            raise ValueError("Title must be under 150 characters; reply text 1–4000 characters.")
        if not (0 <= color <= 0xFFFFFF):
            raise ValueError("Invalid embed colour.")
        with self.conn:
            self.conn.execute(
                """INSERT INTO replies (guild_id, keyword, title, body, color)
                   VALUES (?, ?, ?, ?, ?)
                   ON CONFLICT(guild_id, keyword) DO UPDATE SET
                     title=excluded.title, body=excluded.body, color=excluded.color""",
                (guild_id, keyword, title, body, color),
            )

    def delete(self, guild_id: int, keyword: str) -> bool:
        with self.conn:
            cursor = self.conn.execute("DELETE FROM replies WHERE guild_id=? AND keyword=?",
                                       (guild_id, normalize_keyword(keyword)))
        return cursor.rowcount > 0

    def list(self, guild_id: int) -> list[str]:
        rows = self.conn.execute(
            "SELECT keyword FROM replies WHERE guild_id=? ORDER BY keyword", (guild_id,)
        ).fetchall()
        return [row["keyword"] for row in rows]

    def close(self) -> None:
        self.conn.close()
