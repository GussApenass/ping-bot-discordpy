import aiohttp
import json
import os
from src.functions.dotenv import DISCORD_TOKEN
from src.functions.criar_emoji_shardcloud import criar_emoji_shardcloud

TMP_PATH = "src/tmp/tmp_emoji.json"
EMOJI_NAME = "ShardCloud"

async def obter_mencao_emoji_shardcloud(
    application_id: str,
    emoji_id: int
) -> str:
    headers = {
        "Authorization": f"Bot {DISCORD_TOKEN}",
        "Content-Type": "application/json"
    }

    async def fetch_emoji(session):
        url = f"https://discord.com/api/v10/applications/{application_id}/emojis/{emoji_id}"
        async with session.get(url, headers=headers) as resp:
            if resp.status == 200:
                return await resp.json()
            return None

    async with aiohttp.ClientSession() as session:
        emoji_data = await fetch_emoji(session)

        if emoji_data:
            return f"<:{emoji_data['name']}:{emoji_data['id']}>"

        if os.path.isfile(TMP_PATH):
            os.remove(TMP_PATH)

        novo_emoji = await criar_emoji_shardcloud(DISCORD_TOKEN, application_id)
        novo_id = novo_emoji.get("id")

        if not novo_id:
            return "..."

        emoji_data = await fetch_emoji(session)

        if emoji_data:
            return f"<:{emoji_data['name']}:{emoji_data['id']}>"

    raise Exception("Não foi possível obter a menção do emoji ShardCloud.")