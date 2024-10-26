from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from src.infra.di.container import init_container
from src.presentation.web_api.exc_handlers import setup_exception_handlers
from src.presentation.web_api.handlers.main import setup_handlers


def create_app():
    container = init_container()
    app = FastAPI()

    setup_dishka(container, app)
    setup_handlers(app)
    setup_exception_handlers(app)

    return app
