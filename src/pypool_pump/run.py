# coding: utf-8
"""Run class to manage time interval where the pool pump need to be active.
"""

from datetime import timedelta, datetime


class Run:
    """Represents a single run of the pool pump."""

    def __init__(self, start_time_local_tz, duration_in_hours):
        """Initialise run."""
        self._start_time = start_time_local_tz
        self._duration = duration_in_hours

    def __repr__(self):
        """Return string representation of this feed."""
        return "<{}(start={}, stop={}, duration={})>".format(
            self.__class__.__name__, self.start_time, self.stop_time, self.duration
        )

    @property
    def duration(self):
        """Return duration of this run."""
        return self._duration

    @property
    def start_time(self):
        """Return start time of this run."""
        return self._start_time

    @property
    def stop_time(self):
        """Return stop time of this run."""
        return self.start_time + timedelta(hours=self.duration)

    def run_now(self, local_time):
        """Check if the provided time falls within this run's timeframe."""
        return self.start_time <= local_time < self.stop_time

    def is_next_run(self, local_time):
        """Check if this is the next run after the provided time."""
        return local_time <= self.stop_time

    def pretty_print(self):
        """Provide a usable representation of start and stop time."""
        if self.start_time.day != datetime.now().day:
            start = self.start_time.strftime("%a, %H:%M")
        else:
            start = self.start_time.strftime("%H:%M")
        end = self.stop_time.strftime("%H:%M")
        return "{} - {}".format(start, end)
