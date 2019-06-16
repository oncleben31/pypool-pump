# coding: utf-8
"""tests for pypool_pump module - FilteringDuration"""
import pytest

from pypool_pump import FilteringDuration


def test_temperature_setter_getter():
    """Test getter and setter of the temperature"""
    pool_controler = FilteringDuration()
    pool_controler.pool_mean_temperature = 12

    assert pool_controler.pool_mean_temperature == 12

