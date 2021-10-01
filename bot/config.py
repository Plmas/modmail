import os
from typing import NamedTuple


class BotConfig(NamedTuple):
    token = os.getenv("BOT_TOKEN")
    prefix = os.getenv("PREFIX")
