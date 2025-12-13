import discord
from discord import ui

class LinkTemplateButton(ui.Button):
    def __init__(self, emoji_shardcloud: str):
        super().__init__(
            label="Conheça a Shard Cloud!",
            style=discord.ButtonStyle.link,
            emoji=emoji_shardcloud,
            url="https://shardcloud.app/pt-br/"
        )