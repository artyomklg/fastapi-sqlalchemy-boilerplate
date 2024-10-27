import logging
import sys
from copy import copy
from typing import Literal

import click


class CustomFormatter(logging.Formatter):
    """Logging colored formatter"""

    level_colors = {
        logging.DEBUG: "cyan",
        logging.INFO: "green",
        logging.WARNING: "yellow",
        logging.ERROR: "red",
        logging.CRITICAL: "bright_red",
    }

    def __init__(
        self,
        fmt: str | None = None,
        datefmt: str | None = None,
        style: Literal["%", "{", "$"] = "%",
        use_colors: bool | None = None,
    ):
        if use_colors in (True, False):
            self.use_colors = use_colors
        else:
            self.use_colors = sys.stdout.isatty()
        super().__init__(fmt=fmt, datefmt=datefmt, style=style)

    def formatMessage(self, record: logging.LogRecord) -> str:
        recordcopy = copy(record)
        seperator = " " * (8 - len(recordcopy.levelname))
        recordcopy.levelname = f"{recordcopy.levelname}{seperator}"
        if self.use_colors:
            levelname_color = self.level_colors.get(recordcopy.levelno, "white")
            recordcopy.levelname = click.style(recordcopy.levelname, fg=levelname_color)
        return super().formatMessage(recordcopy)
