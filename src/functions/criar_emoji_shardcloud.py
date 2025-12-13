import aiohttp
import base64
import json
import os
from src.functions.dotenv import DISCORD_TOKEN

EMOJI_NAME = "ShardCloud"
EMOJI_PATH = "src/emojis/ShardCloud.png"
TMP_PATH = "src/tmp/tmp_emoji.json"

async def criar_emoji_shardcloud(application_id: str):
    if os.path.isfile(TMP_PATH):
        with open(TMP_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            if "id" in data:
                return data

    with open(EMOJI_PATH, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()

    payload = {
        "name": EMOJI_NAME,
        "image": f"data:image/png;base64,{image_b64}"
    }

    url = f"https://discord.com/api/v10/applications/{application_id}/emojis"
    headers = {
        "Authorization": f"Bot {DISCORD_TOKEN}",
        "Content-Type": "application/json"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as resp:
            if resp.status not in (200, 201):
                error = await resp.text()
                raise Exception(f"Erro ao criar emoji ({resp.status}): {error}")

            emoji_data = await resp.json()

    os.makedirs(os.path.dirname(TMP_PATH), exist_ok=True)

    with open(TMP_PATH, "w", encoding="utf-8") as f:
        json.dump(
            {
                "id": emoji_data["id"]
            },
            f,
            indent=2
        )

    return emoji_data
