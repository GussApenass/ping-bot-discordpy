import datetime
from zoneinfo import ZoneInfo

class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"

    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

LOG_TYPES = {
    "INFO": {
        "color": Colors.CYAN,
        "emoji": "ℹ️",
        "label": "INFO"
    },
    "WARN": {
        "color": Colors.YELLOW,
        "emoji": "⚠️",
        "label": "WARN"
    },
    "ERROR": {
        "color": Colors.RED,
        "emoji": "❌",
        "label": "ERROR"
    },
    "SUCCESS": {
        "color": Colors.GREEN,
        "emoji": "✅",
        "label": "SUCCESS"
    },
    "DEBUG": {
        "color": Colors.MAGENTA,
        "emoji": "🐞",
        "label": "DEBUG"
    }
}

LIGHT_GRAY = "\033[90m"

def log(text: str, type: str = "WARN"):
    """
    Types suportados:
        - INFO
        - WARN
        - ERROR
        - SUCCESS
        - DEBUG
    """
    t = type.upper()

    info = LOG_TYPES.get(t, LOG_TYPES["INFO"])
    tz = ZoneInfo("America/Sao_Paulo")
    
    timestamp = datetime.datetime.now(tz).strftime("%d/%m/%Y | %H:%M:%S")

    print(
        f"{LIGHT_GRAY}[{timestamp}]{Colors.RESET} "
        f"{Colors.BOLD}{info['color']}{info['emoji']} {info['label']}{Colors.RESET} {text}"
    )