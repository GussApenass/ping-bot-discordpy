import discord
from discord.ext import commands
from src.components.events.mentioned_event.LayoutView.LayoutText import LayoutText

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

        comandos = len(self.bot.tree.get_commands())

        await message.reply(
            view=LayoutText(self.bot, comandos)
        )

async def setup(bot: commands.Bot):
    await bot.add_cog(MentionBot(bot))
