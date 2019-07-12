# coding: utf-8
"""tests for pypool_pump module - PumpCaracteristicFilteringDuration"""
import pytest

from pypool_pump import PumpCaracteristicFilteringDuration


@pytest.mark.parametrize(
    "temperature, duration",
    [
        (-10, 0),
        (0, 0),
        (9, 0),
        (10, 0),
        (12, 2),
        (14, 2),
        (20, 4),
        (25, 8),
        (29, 12),
        (30, 12),
        (50, 12),
    ],
)
def test_pool_caracteristic_duration(temperature, duration):
    """Test duration calculation."""
    pool_controler = PumpCaracteristicFilteringDuration(40, 10)
    assert abs(pool_controler.duration(temperature) - duration) < 0.1


@pytest.mark.parametrize(
    "number_of_bathers, duration", [(0, 4), (2, 4.4), (4, 4.8), (10, 6.0)]
)
def test_pool_caracteristic_duration_with_bathers(number_of_bathers, duration):
    """Test duration calculation."""
    pool_controler = PumpCaracteristicFilteringDuration(40, 10)
    assert abs(pool_controler.duration(20, number_of_bathers) - duration) < 0.1
