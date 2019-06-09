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
    """Dumb calulation method with taking temperaure/2"""

    @property
    def duration(self):
        filtering_duration = self._pool_mean_temperature / 2
        if filtering_duration < 0:
            return 0
        elif filtering_duration > 24:
            return 24
        else:
            return filtering_duration


class BasicFilteringDuration(FilteringDuration):
    """Basic calculation method with temperature/2 and specificities
    below 10°C and above 30°C
    """

    @property
    def duration(self):
        filtering_duration = self._pool_mean_temperature / 2
        if self._pool_mean_temperature < 10:
            # No need to filter below 10°C.
            return 0
        elif self._pool_mean_temperature >= 30:
            # Above 30°C it is recommanded to filter continuously.
            return 24
        else:
            return filtering_duration


# TODO: courbe
# TODO: caractéristique pompe.
# TODO: ajouter modificateur nombre de personne.
