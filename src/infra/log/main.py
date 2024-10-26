import logging

from src.infra.log.config import LogConfig


def setup_logging(conf: LogConfig):
    logging.basicConfig(format=conf.log_format, datefmt=conf.log_datefmt)
    logger = logging.getLogger("src")

    logger.setLevel(conf.log_level)
