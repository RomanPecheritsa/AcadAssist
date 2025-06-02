import logging
import os
from logging.handlers import RotatingFileHandler


def setup_loggers():
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s (%(filename)s:%(lineno)d)")

    # --- app_logger ---
    app_logger = logging.getLogger("app_logger")
    app_logger.setLevel(logging.DEBUG)
    app_handler = RotatingFileHandler(
        os.path.join(log_dir, "app.log"),
        maxBytes=10 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8",
    )
    app_handler.setFormatter(formatter)
    app_logger.addHandler(app_handler)
    app_logger.addHandler(logging.StreamHandler())

    # --- client_logger ---
    client_logger = logging.getLogger("client_logger")
    client_logger.setLevel(logging.INFO)
    client_handler = RotatingFileHandler(
        os.path.join(log_dir, "client_requests.log"),
        maxBytes=10 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8",
    )
    client_handler.setFormatter(formatter)
    client_logger.addHandler(client_handler)
    client_logger.addHandler(logging.StreamHandler())

    # --- sqlalchemy_logger ---
    sql_logger = logging.getLogger("sqlalchemy.engine")
    sql_logger.setLevel(logging.INFO)

    sql_handler = RotatingFileHandler(
        os.path.join(log_dir, "sql_queries.log"),
        maxBytes=10 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )
    sql_handler.setFormatter(formatter)
    sql_logger.addHandler(sql_handler)
    sql_logger.propagate = False

    return {
        "app_logger": app_logger,
        "client_logger": client_logger,
    }


loggers = setup_loggers()
