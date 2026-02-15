import discord
from discord import ui
from discord.ext import commands
from src.functions.dotenv import BOT_PREFIX

class LayoutText(ui.LayoutView):
    def __init__(self, bot: commands.Bot, comandos: int):
        super().__init__(timeout=None)
        self.bot = bot
        self.comandos = comandos
        
        text_display = discord.ui.TextDisplay(content=f"Oi!! Sou o {self.bot.user.name} a companhia perfeita para o seu servidor! Atualmente meu prefixo é **{BOT_PREFIX}** e tenho {self.comandos} comandos registrados (*Slash Commands*)!")
        
        separator = discord.ui.Separator()
        
        self.add_item(text_display)
        self.add_item(separator)