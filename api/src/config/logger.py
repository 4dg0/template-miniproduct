import logging
import logfire
from src.config import env

match env.env:
    case "local":
        level = logging.DEBUG
    case _:
        level = logging.INFO


def init_logger():
    logfire.configure(token=env.logfire_token, environment=env.env, service_name="api")

    logging.basicConfig(
        level=level,
        format="[%(asctime)s] %(levelname)s in %(name)s: %(message)s",
        handlers=[logfire.LogfireLoggingHandler()],
    )
