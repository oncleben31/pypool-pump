# coding: utf-8
"""tests for pypool_pump module - FilteringDuration"""
import pytest

from pypool_pump import FilteringDuration, Run
from datetime import datetime

@pytest.mark.parametrize(
    "pourcentage, result",
    [
        
        (-10,0),
        (0,0),
        (10,1),
        (50,5),
        (100,10),
        (150,15),
        (300,24)
    ],
)
def test_pourcentage(pourcentage, result):
    """Test modifier of the computed duration."""
    pool_controler = FilteringDuration(pourcentage)
    #Fake computed duration for testing.
    pool_controler._computed_filtering_duration = 10
    assert pool_controler.duration() == result

def test_schedule():
    """Test schedule generated."""
    schedule_config = { "break_duration": 3}
    noon = datetime(2020,5,5,12,0)
    pool_controler = FilteringDuration(schedule_config=schedule_config)
    #Fake computed duration for testing.
    pool_controler._total_duration = 6
    assert "{}".format(pool_controler.update_schedule(noon)) == "{}".format([Run(datetime(2020,5,5,9,0),2.0), Run(datetime(2020,5,5,14,0),4.0) ])