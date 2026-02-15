import discord
from discord import ui
from discord.ext import commands

class InitialLayout(ui.LayoutView):
    def __init__(self, bot: commands.Bot, ping: float = None):
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
        )
        self.add_item(c)