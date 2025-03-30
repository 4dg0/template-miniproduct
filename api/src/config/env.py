from pydantic_settings import BaseSettings


class Env(BaseSettings):
    debug: bool = False

    pb_id: str
    pb_url: str
    pb_password: str

    logfire_token: str
    logfire_env: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


env = Env()
