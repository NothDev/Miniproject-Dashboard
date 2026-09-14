import pytest

from services.humidity import classify_humidity


def test_normal():
    assert classify_humidity(50) == "NORMAL"


def test_normal_boundary_low():
    assert classify_humidity(40) == "NORMAL"


def test_normal_boundary_high():
    assert classify_humidity(60) == "NORMAL"


def test_warning_low_side():
    assert classify_humidity(35) == "WARNING"


def test_warning_high_side():
    assert classify_humidity(65) == "WARNING"


def test_critical_low():
    assert classify_humidity(20) == "CRITICAL"


def test_critical_high():
    assert classify_humidity(90) == "CRITICAL"


def test_invalid_below_range():
    with pytest.raises(ValueError):
        classify_humidity(-5)


def test_invalid_above_range():
    with pytest.raises(ValueError):
        classify_humidity(150)
