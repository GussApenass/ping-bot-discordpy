import discord
from discord import ui
from discord.ext import commands
from src.components.slash.ping_command.Buttons.LinkTemplateButton import LinkTemplateButton

class InitialLayout(ui.LayoutView):
    def __init__(self, emoji_shardcloud: str, bot: commands.Bot, ping: float = None):
        super().__init__(timeout=None)

        avatar_url = bot.user.display_avatar.url
        websocket = bot.latency * 1000
        ping_ex = f"{ping:.2f}ms" if ping else "Calculando"

        c = ui.Container(
            ui.Section("## 🏓 **|** Pong!\nVeja o meu ping **a baixo!**", accessory=ui.Thumbnail(
                media=avatar_url
            )),
            ui.Separator(),
            ui.TextDisplay(
                f"📡 **| Websocket**: __{websocket:.2f}ms__"
            ),
            ui.TextDisplay(
                f"💾 **| Latência da API**: __{ping_ex}__\n"
            ),
            ui.Separator(),
            ui.Section(
                f"## {emoji_shardcloud} **|** Shard Cloud!\n"
                "Sabia que eu sou um [template da Shard Cloud](https://shardcloud.app/pt-br/templates)?",
                accessory=LinkTemplateButton(emoji_shardcloud)
            )
        )
        self.add_item(c)