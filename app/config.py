from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:pass@db:5432/pricing"
    VW_PRICE_MAX: int = 500
    ELASTICITY: float = 1.5
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()
