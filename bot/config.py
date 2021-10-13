import os
from typing import NamedTuple
from dotenv import load_dotenv

load_dotenv()


class EnvironmentConfig(NamedTuple):
    token = os.getenv("BOT_TOKEN")
    prefix = os.getenv("PREFIX")
    database_url = os.getenv("DATABASE_URL")
