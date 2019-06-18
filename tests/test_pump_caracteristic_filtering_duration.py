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

