from pydantic_settings import BaseSettings


class Env(BaseSettings):
    service_name: str
    env: str

    pb_id: str
    pb_url: str
    pb_password: str

    logfire_token: str

    stripe_api_key: str
    stripe_webhook_secret: str

    web_url: str

    langfuse_public_key: str
    langfuse_secret_key: str
    langfuse_host: str

    llmproxy_host: str
    llmproxy_api_key: str

    llmmodel_writer: str
    llmmodel_reasoner: str
    llmmodel_small: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def init_env():
    env = Env()
    return env