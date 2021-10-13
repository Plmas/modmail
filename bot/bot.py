import discord
from discord.ext.commands import ExtensionNotFound, Bot
from loguru import logger

from config import EnvironmentConfig
from database.database import db_init

cogs = []


class ModMailBot(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self) -> None:
        logger.info(f"Bot has received ready event and logged in as {self.user}")

    def startup(self) -> None:
        logger.info("Loading extensions...")
        for cog in cogs:
            try:
                self.load_extension(cog)
                logger.info(f"Loaded extension {cog}")
            except ExtensionNotFound:
                logger.error(f"Failed to load extension {cog}")

        self.loop.run_until_complete(db_init())


def main():
    intents = discord.Intents.all()

    bot = ModMailBot(intents=intents, command_prefix=EnvironmentConfig.prefix)

    bot.startup()

    bot.run(EnvironmentConfig.token)


if __name__ == "__main__":
    main()
