from discord.ext import commands
import discord
from discord import app_commands
from src.components.prefix.ping_command.LayoutView.InitialLayout import InitialLayout
import time
from src.functions.obter_mencao_emoji_shardcloud import obter_mencao_emoji_shardcloud
from src.functions.obter_id_emoji_shardcloud import obter_id_emoji_shardcloud

class PingPrefix(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping", aliases=['pinge', 'pingue', 'tempo', 'pong'])
    async def ping_slash(self, ctx: commands.Context):
        emoji_id = obter_id_emoji_shardcloud()
        if not emoji_id:
            await ctx.reply("❌ **|** Ops... Ocorreu um erro ao obter o emoji... Tente novamente mais tarde")

        emoji_shardcloud = await obter_mencao_emoji_shardcloud(self.bot.user.id, emoji_id)

        start = time.perf_counter()

        view = InitialLayout(emoji_shardcloud, self.bot, None)
        message = await ctx.reply(view=view)

        end = time.perf_counter()
        api_latency = (end - start) * 1000

        view2 = InitialLayout(emoji_shardcloud, self.bot, api_latency)
        await message.edit(view=view2)

async def setup(bot: commands.Bot):
    await bot.add_cog(PingPrefix(bot))