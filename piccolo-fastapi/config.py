from pydantic import BaseSettings


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"


settings = Settings()
