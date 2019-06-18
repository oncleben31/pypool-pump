# coding: utf-8
"""tests for pypool_pump module - DumbFilteringDuration"""
import pytest

from pypool_pump import DumbFilteringDuration


@pytest.mark.parametrize(
    "temperature, duration",
    [(-10, 0), (0, 0), (2, 1), (10, 5), (20, 10), (30, 15), (50, 24)],
)
def test_dumb_duration(temperature, duration):
    """Test duration calculation."""
    pool_controler = DumbFilteringDuration()
    assert pool_controler.duration(temperature) == duration

