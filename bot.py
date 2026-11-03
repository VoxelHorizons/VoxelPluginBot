"""Voxel Horizons quick replies: !!keyword [subkey], managed in Discord."""
from __future__ import annotations

import os
import re
import time
from pathlib import Path

import discord
from discord import app_commands

from permissions import has_reply_editor_role
from storage import DEFAULT_COLOR, Reply, ReplyStore, normalize_keyword, parse_color

TOKEN = os.environ.get("DISCORD_TOKEN", "")
TEST_GUILD_ID = os.environ.get("DISCORD_TEST_GUILD_ID")
DATABASE_PATH = Path(os.environ.get("DATABASE_PATH", "data/replies.sqlite3"))
store = ReplyStore(DATABASE_PATH)

# A saved command can appear anywhere in a message, including with extra text.
# The optional next word is treated as a subkey only when that saved reply exists.
INLINE_TRIGGER = re.compile(
    r"!!([a-z0-9_-]{1,32})(?![a-z0-9_-])(?:[ \t]+([a-z0-9_-]{1,32})(?![a-z0-9_-]))?",
    re.IGNORECASE,
)

intents = discord.Intents.default()
intents.message_content = True  # Required for message triggers such as !!logs.


class VoxelReplyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents, allowed_mentions=discord.AllowedMentions.none())
        self.tree = app_commands.CommandTree(self)
        self.last_used: dict[tuple[int, int, str], float] = {}

    async def setup_hook(self) -> None:
        self.tree.add_command(reply_commands)
        if TEST_GUILD_ID:
            guild = discord.Object(id=int(TEST_GUILD_ID))
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
        else:
            await self.tree.sync()

    async def on_ready(self) -> None:
        print(f"VoxelPluginBot ready as {self.user}")

    async def on_message(self, message: discord.Message) -> None:
        if message.guild is None or message.author.bot:
            return
        # Scan for the first *saved* command anywhere in the message.
        # Prefer the optional subkey when it exists; otherwise use the base
        # reply, even if unrelated words follow (e.g. "!!support please help").
        keyword = None
        reply = None
        for match in INLINE_TRIGGER.finditer(message.content):
            base = match.group(1).lower()
            subkey = match.group(2)
            if subkey:
                candidate = f"{base} {subkey.lower()}"
                reply = store.get(message.guild.id, candidate)
                if reply:
                    keyword = candidate
                    break
            reply = store.get(message.guild.id, base)
            if reply:
                keyword = base
                break
        if not reply:
            return
        # Guard against someone repeatedly invoking the same canned responses.
        # Apply cooldown to a specific saved reply, not every command from this user.
        # This lets !!support and !!support furniture work back-to-back.
        key = (message.guild.id, message.author.id, keyword)
        now = time.monotonic()
        if now - self.last_used.get(key, -999.0) < 5:
            return
        self.last_used[key] = now
        try:
            await message.reply(
                embed=render_reply(reply, message),
                mention_author=False,
                allowed_mentions=discord.AllowedMentions.none(),
            )
        except discord.Forbidden:
            print(f"Missing Send Messages/Embed Links in channel {message.channel.id}")


def render_reply(reply: Reply, message: discord.Message | discord.Interaction) -> discord.Embed:
    text = reply.body
    author = message.author if isinstance(message, discord.Message) else message.user
    placeholders = {
        "{{user}}": author.display_name,
        "{{server}}": message.guild.name if message.guild else "",
        "{{channel}}": getattr(message.channel, "name", "channel"),
    }
    for key, value in placeholders.items():
        text = text.replace(key, value)
    return discord.Embed(title=reply.title or None, description=text, color=reply.color)


def can_manage(interaction: discord.Interaction) -> bool:
    return (
        interaction.guild is not None
        and isinstance(interaction.user, discord.Member)
        and interaction.user.guild_permissions.manage_messages
    )


async def require_staff(interaction: discord.Interaction) -> bool:
    if can_manage(interaction):
        return True
    await interaction.response.send_message(
        "You need the **Manage Messages** permission to manage support replies.", ephemeral=True
    )
    return False


async def require_reply_editor(interaction: discord.Interaction) -> bool:
    """Require Plugin Developer or Contributor, independent of Manage Messages."""
    if (
        interaction.guild is not None
        and isinstance(interaction.user, discord.Member)
        and has_reply_editor_role(role.id for role in interaction.user.roles)
    ):
        return True
    await interaction.response.send_message(
        "Only members with the **Plugin Developer** or **Contributor** role "
        "can create or edit support replies.",
        ephemeral=True,
    )
    return False


async def validated_keyword(
    interaction: discord.Interaction, text: str, subkey: str | None = None
) -> str | None:
    try:
        return normalize_keyword(f"{text} {subkey}" if subkey else text)
    except ValueError as exc:
        await interaction.response.send_message(str(exc), ephemeral=True)
        return None


class ReplyModal(discord.ui.Modal):
    def __init__(self, guild_id: int, keyword: str, existing: Reply | None):
        self.guild_id = guild_id
        self.keyword = keyword
        self.existing = existing
        label = "Edit" if existing else "Create"
        super().__init__(title=f"{label} !!{keyword}"[:45])
        self.reply_title = discord.ui.TextInput(
            label="Embed title (optional)", required=False, max_length=150,
            default=existing.title if existing else "", placeholder="Leave blank for no title",
        )
        self.reply_body = discord.ui.TextInput(
            label="Support reply (Markdown supported)",
            style=discord.TextStyle.paragraph, required=True, max_length=4000,
            default=existing.body if existing else None,
            placeholder="Enter the reply shown when someone types !!" + keyword,
        )
        self.reply_color = discord.ui.TextInput(
            label="Embed colour (hex)", required=True, min_length=6, max_length=7,
            default=f"{existing.color if existing else DEFAULT_COLOR:06X}",
        )
        self.add_item(self.reply_title)
        self.add_item(self.reply_body)
        self.add_item(self.reply_color)

    async def on_submit(self, interaction: discord.Interaction) -> None:
        if not await require_reply_editor(interaction):
            return
        if interaction.guild_id != self.guild_id:
            await interaction.response.send_message("This form belongs to another server.", ephemeral=True)
            return
        try:
            color = parse_color(str(self.reply_color.value))
            store.save(self.guild_id, self.keyword,
                       str(self.reply_title.value), str(self.reply_body.value), color)
        except ValueError as exc:
            await interaction.response.send_message(str(exc), ephemeral=True)
            return
        await interaction.response.send_message(
            f"Saved **!!{self.keyword}**. Type it in an existing support thread to test.",
            ephemeral=True,
        )


reply_commands = app_commands.Group(
    name="reply", description="Create and manage reusable support replies",
    guild_only=True,
)


@reply_commands.command(name="create", description="Create a !!keyword or !!keyword subkey reply")
@app_commands.describe(
    keyword="Base command, e.g. support",
    subkey="Optional specific topic, e.g. furniture",
)
async def create_reply(
    interaction: discord.Interaction, keyword: str, subkey: str | None = None
) -> None:
    if not await require_reply_editor(interaction):
        return
    keyword = await validated_keyword(interaction, keyword, subkey)
    if keyword is None:
        return
    if store.get(interaction.guild_id, keyword):
        await interaction.response.send_message(
            f"**!!{keyword}** exists. Use `/reply edit` instead.", ephemeral=True
        )
        return
    await interaction.response.send_modal(ReplyModal(interaction.guild_id, keyword, None))


@reply_commands.command(name="edit", description="Edit a saved reply, including an optional subkey")
@app_commands.describe(
    keyword="Base command, e.g. support",
    subkey="Optional specific topic, e.g. furniture",
)
async def edit_reply(
    interaction: discord.Interaction, keyword: str, subkey: str | None = None
) -> None:
    if not await require_reply_editor(interaction):
        return
    keyword = await validated_keyword(interaction, keyword, subkey)
    if keyword is None:
        return
    existing = store.get(interaction.guild_id, keyword)
    if not existing:
        await interaction.response.send_message("That reply doesn't exist.", ephemeral=True)
        return
    await interaction.response.send_modal(ReplyModal(interaction.guild_id, keyword, existing))


@reply_commands.command(name="delete", description="Delete a saved reply, including an optional subkey")
@app_commands.describe(
    keyword="Base command, e.g. support",
    subkey="Optional specific topic, e.g. furniture",
)
async def delete_reply(
    interaction: discord.Interaction, keyword: str, subkey: str | None = None
) -> None:
    if not await require_staff(interaction):
        return
    keyword = await validated_keyword(interaction, keyword, subkey)
    if keyword is None:
        return
    deleted = store.delete(interaction.guild_id, keyword)
    await interaction.response.send_message(
        f"Deleted **!!{keyword}**." if deleted else "That reply doesn't exist.",
        ephemeral=True,
    )


@reply_commands.command(name="list", description="List available support replies")
async def list_replies(interaction: discord.Interaction) -> None:
    if not await require_staff(interaction):
        return
    keywords = store.list(interaction.guild_id)
    result = ", ".join(f"`!!{keyword}`" for keyword in keywords)
    await interaction.response.send_message(result[:1900] or "No replies yet.", ephemeral=True)


@reply_commands.command(name="preview", description="Preview a reply, including an optional subkey")
@app_commands.describe(
    keyword="Base command, e.g. support",
    subkey="Optional specific topic, e.g. furniture",
)
async def preview_reply(
    interaction: discord.Interaction, keyword: str, subkey: str | None = None
) -> None:
    if not await require_staff(interaction):
        return
    keyword = await validated_keyword(interaction, keyword, subkey)
    if keyword is None:
        return
    reply = store.get(interaction.guild_id, keyword)
    if not reply:
        await interaction.response.send_message("That reply doesn't exist.", ephemeral=True)
        return
    # Create a preview with the same placeholders as a real invocation.
    await interaction.response.send_message(
        f"Preview: `!!{keyword}`", embed=render_reply(reply, interaction), ephemeral=True,
        allowed_mentions=discord.AllowedMentions.none(),
    )


if __name__ == "__main__":
    if not TOKEN:
        raise SystemExit("Set DISCORD_TOKEN in the environment before starting the bot.")
    VoxelReplyBot().run(TOKEN)
