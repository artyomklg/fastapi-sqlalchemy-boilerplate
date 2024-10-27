import logging
import logging.config
import sys

from src.infra.log.config import LogConfig
from src.infra.log.formatter import CustomFormatter


def setup_logging(log_conf: LogConfig) -> None:
    color_formatter = CustomFormatter(
        fmt=log_conf.format,
        datefmt=log_conf.datefmt,
        use_colors=log_conf.use_colors,
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(color_formatter)

    loggers = (
        logging.root.name,
        "src",
        "uvicorn",
        "uvicorn.error",
        "uvicorn.access",
    )
    for logger_name in loggers:
        cur_logger = logging.getLogger(logger_name)
        cur_logger.setLevel(log_conf.level)
        cur_logger.handlers = [handler]
        cur_logger.propagate = False
