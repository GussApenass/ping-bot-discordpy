from discord.ext import commands
import discord
from discord import app_commands
from src.components.slash.ping_command.LayoutView.InitialLayout import InitialLayout
import time

class PingSlash(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Bora ver meu ping? Só usar o comando!")
    async def ping_slash(self, interaction: discord.Interaction):
        await interaction.response.defer()

        start = time.perf_counter()
        
        view = InitialLayout(self.bot, None)
        await interaction.edit_original_response(view=view)
        end = time.perf_counter()

        api_latency = (end - start) * 1000
        
        view2 = InitialLayout(self.bot, api_latency)
        msg = await interaction.original_response()
        await msg.edit(view=view2)

async def setup(bot: commands.Bot):
    await bot.add_cog(PingSlash(bot))