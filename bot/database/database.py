from loguru import logger
from tortoise import Tortoise
from database.config import TORTOISE_CONFIG


async def db_init() -> None:
    """Generates database tables."""
    await Tortoise.init(config=TORTOISE_CONFIG)

    await Tortoise.generate_schemas()

    logger.info("Database synced")
