""" Configuration file for pytest. """
import os

import pytest


_IMPLICIT_WAIT = 20
SCREEN_RESOLUTION = (1600, 900)


if os.getenv('TRAVIS', None):
    from pyvirtualdisplay import Display
    display = Display(visible=0, size=SCREEN_RESOLUTION)
    display.start()


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument('--headless')
    return chrome_options
