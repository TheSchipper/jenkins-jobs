import pytest
import logging
import atexit
import logging.config
import json


def _get_logging_config():
    with open("../log-configuration.json", "r") as f:
        return json.load(f)


def pytest_configure(config):
    logging.config.dictConfig(_get_logging_config())
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)

    pytest.logger = logging.getLogger()

