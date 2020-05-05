# coding: utf-8
"""tests for pypool_pump module - AbacusFilteringDuration"""

import pytest

from pypool_pump import AbacusFilteringDuration


@pytest.mark.parametrize(
    "temperature, duration",
    [
        (-10, 2),
        (0, 2),
        (9, 2),
        (10, 2),
        (12, 2.7),
        (14, 3.2),
        (20, 5),
        (25, 9),
        (29, 15.8),
        (30, 18.2),
        (50, 24),
    ],
)
def test_abacus_duration(temperature, duration):
    """Test duration calculation."""
    pool_controler = AbacusFilteringDuration()
    # assert pool_controler.duration == duration
    assert abs(pool_controler.duration(temperature) - duration) < 0.1
