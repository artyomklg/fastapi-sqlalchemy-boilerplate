import logging

from src.infra.log.config import LogConfig


def setup_logging(log_conf: LogConfig) -> None:
    logging.basicConfig(format=log_conf.format, datefmt=log_conf.datefmt)
    logger = logging.getLogger("src")

    logger.setLevel(log_conf.level)
