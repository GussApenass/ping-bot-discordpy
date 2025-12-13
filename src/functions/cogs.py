import time
import os
from src.functions.log import log

PASTAS = [
    "src.commands.slash",
    "src.commands.prefix",
    "src.events"
]

async def load_cogs(bot):
    inicio = time.perf_counter()
    carregadas = 0
    erros = []

    for pasta in PASTAS:
        pasta_path = pasta.replace(".", os.sep)

        if not os.path.isdir(pasta_path):
            log(f"Pasta não encontrada: {pasta}", "WARN")
            continue

        for root, _, files in os.walk(pasta_path):
            for file in files:
                if not file.endswith(".py") or file.startswith("_"):
                    continue

                caminho_completo = os.path.join(root, file)

                modulo = (
                    caminho_completo
                    .replace(os.sep, ".")
                    .replace(".py", "")
                )

                try:
                    await bot.load_extension(modulo)
                    carregadas += 1
                    log(f"Cog carregada: {modulo}", "SUCCESS")

                except Exception as e:
                    erros.append((modulo, str(e)))
                    log(f"Erro ao carregar {modulo}: {e}", "ERROR")

    await bot.tree.sync()

    tempo_total = time.perf_counter() - inicio
    
    log(f"Tempo total: {tempo_total:.2f}s", "INFO")
    log(f"Cogs carregadas: {carregadas}", "INFO")
    log(f"Falhas: {len(erros)}", "ERROR")

    if erros:
        log("🧾 Lista de falhas:", "WARN")
        for modulo, erro in erros:
            log(f" - {modulo}: {erro}", "WARN")