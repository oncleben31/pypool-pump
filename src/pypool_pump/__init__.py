# coding: utf-8
"""pypool_pump package allows to compute the duration of the swiming pool
filtering.
"""


class FilteringDuration(object):
    """Root class with common parts"""

    def __init__(self, temperature=None):
        self._pool_mean_temperature = temperature
        self._filtering_duration = None

    @property
    def duration(self):
        return self._filtering_duration

    @property
    def pool_mean_temperature(self):
        return self._pool_mean_temperature

    @pool_mean_temperature.setter
    def pool_mean_temperature(self, temperature):
        self._pool_mean_temperature = temperature


class DumbFilteringDuration(FilteringDuration):
    """Basic calulation method with taking temperaure/2"""

    @property
    def duration(self):
        filtering_duration = self._pool_mean_temperature / 2
        if filtering_duration < 0:
            return 0
        elif filtering_duration > 24:
            return 24
        else:
            return filtering_duration


# TODO: basic min < 10° / /2  / 24 > 30°
# TODO: courbe
# TODO: caractéristique pompe.

