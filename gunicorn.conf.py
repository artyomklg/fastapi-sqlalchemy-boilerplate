bind = "0.0.0.0:8000"
workers = 2
loglevel = "info"
graceful_timeout = 300
worker_class = "uvicorn.workers.UvicornWorker"
accesslog = "-"
