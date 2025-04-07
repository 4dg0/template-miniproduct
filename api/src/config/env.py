from pydantic_settings import BaseSettings


class Env(BaseSettings):
    env: str

    pb_id: str
    pb_url: str
    pb_password: str

    logfire_token: str

    stripe_api_key: str
    stripe_webhook_secret: str

    web_url: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


env = Env()
