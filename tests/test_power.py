import pytest

from services.power import calculate_power, classify_power

def test_calculate_power():
    assert calculate_power(220, 2.5) == 550


def test_classify_power_normal():
    assert classify_power(499.9) == "NORMAL"


def test_classify_power_warning():
    assert classify_power(500) == "WARNING"
    assert classify_power(1000) == "WARNING"


def test_classify_power_critical():
    assert classify_power(1000.1) == "CRITICAL"


def test_calculate_power_invalid():
    with pytest.raises(ValueError):
        calculate_power(0, 2)
    with pytest.raises(ValueError):
        calculate_power(220, -1)
