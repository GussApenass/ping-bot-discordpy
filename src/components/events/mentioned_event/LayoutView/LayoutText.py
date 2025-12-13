import discord
from discord import ui
from discord.ext import commands
from src.components.events.mentioned_event.Buttons.LinkShardCloudButton import LinkShardCloudButton
from src.functions.dotenv import BOT_PREFIX

class LayoutText(ui.LayoutView):
    def __init__(self, bot: commands.Bot, emoji_shardcloud: str, comandos: int):
        super().__init__(timeout=None)
        self.bot = bot
        self.comandos = comandos
        
        text_display = discord.ui.TextDisplay(content=f"Oi!! Sou o {self.bot.user.name} a companhia perfeita para o seu servidor! Atualmente meu prefixo é **{BOT_PREFIX}** e tenho {self.comandos} comandos registrados (*Slash Commands*)!")
        
        separator = discord.ui.Separator()
        
        section = discord.ui.Section(
            discord.ui.TextDisplay(content=f"{emoji_shardcloud} **|** Ei! Sabia que eu sou um [template da Shard Cloud?](https://shardcloud.app/pt-br/templates)"),
            accessory=LinkShardCloudButton(emoji_shardcloud)
        )
        self.add_item(text_display)
        self.add_item(separator)
        self.add_item(section)