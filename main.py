import discord
from discord.ext import commands, tasks
from src.functions.dotenv import DISCORD_TOKEN, BOT_PREFIX
from src.functions.cogs import load_cogs
from src.functions.log import log
from src.functions.criar_emoji_shardcloud import criar_emoji_shardcloud
import random

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=discord.Intents.all()) # Ative TODOS intents no discord dev, para que possa funcionar

TEXTOS = [
    "Estou Online!",
    "Ahhh, a vida é bela!",
    "Vivendo e aprendendo...",
    "To com sono ;("
]

@bot.event
async def on_ready():
    log(f"[ON] Bot Online como {bot.user.name} ({bot.user.id})", "SUCCESS")
    await load_cogs(bot)
    if not mudar_status.is_running():
        mudar_status.start()
    await criar_emoji_shardcloud(bot.user.id)

@tasks.loop(seconds=30)
async def mudar_status():
    
    frase = random.choice(TEXTOS)

    await bot.change_presence(
        activity=discord.CustomActivity(
            name=frase
        )
    )

bot.run(DISCORD_TOKEN)