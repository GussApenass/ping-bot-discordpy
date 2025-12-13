import discord
from discord.ext import commands
from src.components.events.mentioned_event.LayoutView.LayoutText import LayoutText
from src.functions.obter_id_emoji_shardcloud import obter_id_emoji_shardcloud
from src.functions.obter_mencao_emoji_shardcloud import obter_mencao_emoji_shardcloud

class MentionBot(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        if not self.bot.user:
            return

        content = message.content.strip()

        mention_1 = f"<@{self.bot.user.id}>"
        mention_2 = f"<@!{self.bot.user.id}>"

        if content not in (mention_1, mention_2):
            return

        id = obter_id_emoji_shardcloud()

        emoji_shardcloud = await obter_mencao_emoji_shardcloud(self.bot.user.id, id)

        comandos = len(self.bot.tree.get_commands())

        await message.reply(
            view=LayoutText(self.bot, emoji_shardcloud, comandos)
        )

async def setup(bot: commands.Bot):
    await bot.add_cog(MentionBot(bot))
