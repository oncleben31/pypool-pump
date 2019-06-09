# coding: utf-8
"""tests for pypool_pump module - BasicFilteringDuration"""
import pytest

from pypool_pump import BasicFilteringDuration


@pytest.mark.parametrize(
    "temperature, duration",
    [
        (-10, 0),
        (0, 0),
        (2, 0),
        (9, 0),
        (10, 5),
        (20, 10),
        (29, 14.5),
        (30, 24),
        (50, 24),
    ],
)
def test_basic_duration(temperature, duration):
    """Test duration calculation."""
    pool_controler = BasicFilteringDuration(temperature)
    assert pool_controler.duration == duration

