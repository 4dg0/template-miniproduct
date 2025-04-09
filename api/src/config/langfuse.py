from langfuse import Langfuse

from src.config import Env


def init_langfuse(env: Env):
    langfuse = Langfuse(
        secret_key=env.langfuse_secret_key,
        public_key=env.langfuse_public_key,
        host=env.langfuse_host,
    )
    return langfuse
