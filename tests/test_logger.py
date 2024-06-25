from cliologging import logger
import logging
from pathlib import Path
import re
import os

NAME_LOGGER = "test"
FILE_LOGGER_PATH = Path("debug.log")
PATTERN_DEBUG_LINE = r'^\d+ \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{4} DEBUG\s+ In:[\w-]+|\d+ : test debug level$'
PATTERN_INFO_LINE = r'^\d+ \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{4} INFO\s+ In:[\w-]+|\d+ : test info level$'
PATTERN_WARNING_LINE = r'^\d+ \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{4} WARNING\s+ In:[\w-]+|\d+ : test warning level$'
PATTERN_ERROR_LINE = r'^\d+ \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{4} ERROR\s+ In:[\w-]+|\d+ : test error level$'
PATTERN_CRITICAL_LINE = r'^\d+ \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{4} CRITICAL\s* In:[\w-]+|\d+ : test critical level$'


def test_create():
    # Instance a logger object.
    test_logger = logger.create(NAME_LOGGER, FILE_LOGGER_PATH)

    # Assert : if the variable logger is not a logger object
    assert type(test_logger) is logging.Logger, "The logger created is not a Logger object."

    # Log in log file with every logging level.
    test_logger.debug("test debug level")
    test_logger.info("test info level")
    test_logger.warning("test warning level")
    test_logger.error("test error level")
    test_logger.critical("test critical level")

    # Assert : if the
    with open(FILE_LOGGER_PATH, 'r') as log_file:
        assert re.match(PATTERN_DEBUG_LINE, log_file.readline()), "Debug logging level don't work."
        assert re.match(PATTERN_INFO_LINE, log_file.readline()), "Info logging level don't work."
        assert re.match(PATTERN_WARNING_LINE, log_file.readline()), "Warning logging level don't work."
        assert re.match(PATTERN_ERROR_LINE, log_file.readline()), "Error logging level don't work."
        assert re.match(PATTERN_CRITICAL_LINE, log_file.readline()), "Critical logging level don't work."

    os.remove(FILE_LOGGER_PATH)
