import pytest
import time


def test_logging():
    pytest.logger.info("This is an info message")
    pytest.logger.debug("This is a debug message")
    pytest.logger.warning("This is a warning message")
    pytest.logger.error("This is an error message")
    pytest.logger.critical("This is a critical message")
