# coding: utf-8
"""tests for pypool_pump module - Run class"""

import pytest
from datetime import datetime, timedelta

from pypool_pump import Run

def test_run_propeties():
    """Test Run() properties"""
    date = datetime(2020,5,5,12,0)
    duration_in_minutes = 65
    run = Run(date, duration_in_minutes)

    assert [run.start_time, run.duration, run.stop_time] == [date, duration_in_minutes, datetime(2020,5,5,13,5,0)]

@pytest.mark.parametrize(
    "curent_time, state",
    [
        (datetime(2020,5,4,12,0), False),
        (datetime(2020,5,5,11,59), False),
        (datetime(2020,5,5,12,0), True),
        (datetime(2020,5,5,12,10), True),
        (datetime(2020,5,5,13,0), True),
        (datetime(2020,5,5,13,4,59), True),
        (datetime(2020,5,5,13,5), False),
        (datetime(2020,5,5,13,6), False),
        (datetime(2020,5,6,12,50), False),
    ],
)
def test_run_now(curent_time,state):
    """Test Run() run_now() methods"""
    date = datetime(2020,5,5,12,0)
    duration_in_minutes = 65
    run = Run(date, duration_in_minutes)

    assert run.run_now(curent_time) == state

@pytest.mark.parametrize(
    "curent_time, state",
    [
        (datetime(2020,5,4,12,0), True),
        (datetime(2020,5,5,11,59), True),
        (datetime(2020,5,5,12,0), True),
        (datetime(2020,5,5,12,10), True),
        (datetime(2020,5,5,13,0), True),
        (datetime(2020,5,5,13,4,59), True),
        (datetime(2020,5,5,13,5), True),
        (datetime(2020,5,5,13,6), False),
        (datetime(2020,5,6,12,50), False),
    ],
)
def test_run_is_next_run(curent_time, state):
    """ Test Run() is_next_run() methods"""
    date = datetime(2020,5,5,12,0)
    duration_in_minutes = 65
    run = Run(date, duration_in_minutes)

    assert run.is_next_run(curent_time) == state

def test_run_print():
    """ Test Run() prints methods"""
    date = datetime(2020,5,5,12,0)
    duration_in_minutes = 65
    run = Run(date, duration_in_minutes)

    assert "{}".format(run) == "<Run(start={}, stop={}, duration=65)>".format(datetime(2020,5,5,12,0),datetime(2020,5,5,13,5))

def test_run_pretty_print():
    """ Test Run() prints methods"""
    date = datetime.now()
    date2 = date + timedelta(days=2)
    duration_in_minutes = 65
    run1 = Run(date, duration_in_minutes)
    run2 = Run(date2, duration_in_minutes)

    assert [run1.pretty_print(), run2.pretty_print() ] == [
            "{} - {}".format(date.strftime("%H:%M"), (date + timedelta(minutes=65)).strftime("%H:%M")),
            "{} - {}".format(date2.strftime("%a, %H:%M"), (date2 + timedelta(minutes=65)).strftime("%H:%M")),
            ]