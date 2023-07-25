from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    POSTGRES_DB_NAME: str
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_USER: str
    POSTGRES_HOST: str

    class Config:
        env_file = "/.env"


settings = Settings()
