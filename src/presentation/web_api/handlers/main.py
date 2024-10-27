from fastapi import FastAPI

from src.presentation.web_api.handlers.default import default_router
from src.presentation.web_api.handlers.docs import register_static_docs_routes
from src.presentation.web_api.handlers.exceptions import setup_exception_handlers
from src.presentation.web_api.handlers.healthcheck import healthcheck_router


def setup_handlers(app: FastAPI):
    register_static_docs_routes(app)

    app.include_router(default_router)
    app.include_router(healthcheck_router)
    setup_exception_handlers(app)
