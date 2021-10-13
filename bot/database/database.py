from loguru import logger
from tortoise import Tortoise
from config import EnvironmentConfig


async def db_init() -> None:
    """Generates database tables."""
    await Tortoise.init(
        db_url=EnvironmentConfig.database_url, modules={"models": ["database.models"]}
    )

    await Tortoise.generate_schemas()

    logger.info("Database synced")
