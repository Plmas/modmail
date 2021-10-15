import importlib
import inspect
import os
import pkgutil

import disnake
from disnake.ext.commands import ExtensionNotFound, ExtensionError
from disnake.ext import commands
from loguru import logger
import cogs

from config import EnvironmentConfig
from database.database import db_init


class ModMailBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self) -> None:
        logger.info(f"Bot has received ready event and logged in as {self.user}")

    def load_extensions(self) -> None:
        for file in os.listdir("cogs"):
            if file.endswith(".py"):
                cog = f"cogs.{file[:-3]}"
                try:
                    self.load_extension(cog)
                    logger.info(f"Loaded extension {cog}")
                except ExtensionError as e:
                    logger.error(f"Failed to load extension {e}")

    def startup(self) -> None:
        self.load_extensions()

        self.loop.run_until_complete(db_init())


def main():
    intents = disnake.Intents.all()

    bot = ModMailBot(intents=intents, command_prefix=EnvironmentConfig.prefix)

    bot.startup()

    bot.run(EnvironmentConfig.token)


if __name__ == "__main__":
    main()
