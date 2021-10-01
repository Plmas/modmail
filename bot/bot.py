import discord
from discord.ext.commands import ExtensionNotFound, Bot
from loguru import logger

from config import BotConfig

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


def main():
    intents = discord.Intents.all()

    bot = ModMailBot(intents=intents, command_prefix=BotConfig.prefix)

    bot.startup()

    bot.run(BotConfig.token)


if __name__ == "__main__":
    main()
