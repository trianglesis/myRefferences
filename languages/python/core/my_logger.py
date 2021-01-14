"""
Octopus logger to track:
- all intra-operations
- all external operations
etc.
"""

import datetime
import logging
import os

now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')
place = os.path.normpath('D:/Projects/PycharmProjects/myRefferences/logs/')


def test_logger(name, mode, path=None):
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    if not path:
        path = place
    log_name = os.path.normpath(f"{path}/{name}.log")

    # Extra detailed logging to file:
    f_handler = logging.FileHandler(log_name, mode=mode, encoding='utf-8')

    f_handler.setLevel(logging.DEBUG)
    # Extra detailed logging to console:
    f_format = logging.Formatter(
        '{asctime:<24}'
        '{levelname:<8}'
        '{filename:<20}'
        '{funcName:<22}'
        'L:{lineno:<6}'
        '{message:8s}',
        style='{'
    )

    f_handler.setFormatter(f_format)
    log.addHandler(f_handler)

    return log
