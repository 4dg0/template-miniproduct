import logging
import sys
from pythonjsonlogger import jsonlogger
import logfire

from src.config import Env


class DefaultContextFilter(logging.Filter):
    def __init__(self, env: str, service_name: str):
        super().__init__()
        self.env = env
        self.service_name = service_name

    def filter(self, record: logging.LogRecord) -> bool:
        record.env = self.env
        record.service_name = self.service_name
        record.module_name = record.name
        return True


def init_logging(env: Env):
    logfire.configure(
        service_name=env.service_name,
        send_to_logfire=False,
    )

    if env.env == "local":
        level = logging.DEBUG
    else:
        level = logging.INFO

    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.handlers.clear()

    console_handler = logging.StreamHandler(sys.stdout)
    json_formatter = jsonlogger.JsonFormatter(
        fmt=(
            "%(asctime)s "
            "%(levelname)s "
            "%(module_name)s "
            "%(message)s "
            "%(env)s "
            "%(service_name)s "
            "%(user_id)s "
            "%(request_id)s "
            "%(session_id)s"
        ),
        rename_fields={"asctime": "timestamp"},
    )

    console_handler.setFormatter(json_formatter)
    console_handler.addFilter(DefaultContextFilter(env.env, env.service_name))
    root_logger.addHandler(console_handler)


def get_logger(name: str = None) -> logging.Logger:
    return logging.getLogger(name)
