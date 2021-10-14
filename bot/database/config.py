from config import EnvironmentConfig

TORTOISE_CONFIG = {
    "connections": {"default": EnvironmentConfig.database_url},
    "apps": {
        "models": {"models": ["database.models"]},
    },
}
