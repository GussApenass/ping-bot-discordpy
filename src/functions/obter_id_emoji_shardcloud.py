import json
import os

TMP_PATH = "src/tmp/tmp_emoji.json"

def obter_id_emoji_shardcloud() -> int:
    if not os.path.isfile(TMP_PATH):
        raise FileNotFoundError("Arquivo tmp_emoji.json não encontrado")

    with open(TMP_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    emoji_id = data.get("id")

    if not emoji_id:
        raise ValueError("ID do emoji ShardCloud não encontrado no arquivo, reinicie o bot para que a criação seja concluida.")

    return int(emoji_id)