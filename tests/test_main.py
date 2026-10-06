from main import calculate_wpm, calculate_accuracy


def test_calculate_wpm():
    assert calculate_wpm(300, 60) == 60


def test_zero_time():
    assert calculate_wpm(300, 0) == 0


def test_perfect_accuracy():
    assert calculate_accuracy(100, 100) == 100


def test_partial_accuracy():
    assert calculate_accuracy(88, 100) == 88


def test_decimal_accuracy():
    assert calculate_accuracy(15, 20) == 75


def test_zero_accuracy():
    assert calculate_accuracy(0, 10) == 0


def test_zero_total():
    assert calculate_accuracy(0, 0) == 0