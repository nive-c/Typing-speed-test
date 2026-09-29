# tests/test_main.py

from main import calculate_wpm


def test_calculate_wpm():
    assert calculate_wpm(300, 60) == 60


def test_zero_time():
    assert calculate_wpm(300, 0) == 0