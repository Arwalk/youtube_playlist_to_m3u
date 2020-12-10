# -*- coding: utf-8 -*-

import pytest
from youtube_playlist_to_m3u.skeleton import fib

__author__ = "Arwalk"
__copyright__ = "Arwalk"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
