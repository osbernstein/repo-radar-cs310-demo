import random

from app import add


def test_add():
    assert add(2, 3) == 5


def test_flaky():
    # Fails about half the time on purpose, for the flaky-test demo.
    assert random.random() < 0.5
