import logging

from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from src.infra.di.container import init_container
from src.infra.log.main import setup_logging
from src.infra.main_config import setup_main_config
from src.presentation.web_api.exc_handlers import setup_exception_handlers
from src.presentation.web_api.handlers.main import setup_handlers

logger = logging.getLogger(__name__)


def create_app():
    main_config = setup_main_config()

    setup_logging(main_config.log)
    logger.info("%s" % main_config)

    container = init_container()
    app = FastAPI()

    setup_dishka(container, app)
    setup_handlers(app)
    setup_exception_handlers(app)

    return app
