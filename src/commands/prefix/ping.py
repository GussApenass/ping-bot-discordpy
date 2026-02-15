from discord.ext import commands
import discord
from discord import app_commands
from src.components.prefix.ping_command.LayoutView.InitialLayout import InitialLayout
import time

class PingPrefix(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping", aliases=['pinge', 'pingue', 'tempo', 'pong'])
    async def ping_slash(self, ctx: commands.Context):

        start = time.perf_counter()

        view = InitialLayout(self.bot, None)
        message = await ctx.reply(view=view)

        end = time.perf_counter()
        api_latency = (end - start) * 1000

        view2 = InitialLayout(self.bot, api_latency)
        await message.edit(view=view2)

async def setup(bot: commands.Bot):
    await bot.add_cog(PingPrefix(bot))