# coding: utf-8
"""pypool_pump package allows to compute the duration of the swiming pool
filtering.
"""

from .__version__ import __version__, VERSION


class FilteringDuration(object):
    """Root class with common parts"""

    def __init__(self, temperature: float = None, percentage: float = None):
        self._pool_mean_temperature = temperature
        self._computed_filtering_duration = None
        self._modifier_pecentage = percentage

    @property
    def duration(self) -> float:
        """Filtering duration in hours
        
        If modifier have been set, they will be applied to the computed filtering
        duration.
        Maximum duration is always 24 hours.
        """
        if self._modifier_pecentage is None:
            return min(self._computed_filtering_duration, 24)
        else:
            return min(
                self._computed_filtering_duration * self._modifier_pecentage / 100, 24
            )

    @property
    def pool_mean_temperature(self) -> float:
        """Pool temerature in °C"""
        return self._pool_mean_temperature

    @pool_mean_temperature.setter
    def pool_mean_temperature(self, temperature: float):
        """Setter for pool temperature in °C"""
        self._pool_mean_temperature = temperature


class DumbFilteringDuration(FilteringDuration):
    """Dumb duration calulation method with taking temperature/2"""

    @property
    def duration(self) -> float:
        """Filtering duration in hours"""
        filtering_duration = self._pool_mean_temperature / 2
        if filtering_duration < 0:
            self._computed_filtering_duration = 0
        else:
            self._computed_filtering_duration = filtering_duration

        return super().duration


class BasicFilteringDuration(FilteringDuration):
    """Basic duration calculation method with:
    - 0 below 10°C
    - temperature/3 between 10°C and 14°C
    - temperature/2 between 14°C and 30°C
    - continuous filtration above 30°C
    """

    @property
    def duration(self) -> float:
        """Filtering duration in hours"""
        if self._pool_mean_temperature < 10:
            # No need to filter below 10°C.
            self._computed_filtering_duration = 0
        elif self._pool_mean_temperature < 14:
            # between 10 and 14 we can reduce filtering
            self._computed_filtering_duration = self._pool_mean_temperature / 3
        elif self._pool_mean_temperature >= 30:
            # Above 30°C it is recommanded to filter continuously.
            self._computed_filtering_duration = 24
        else:
            self._computed_filtering_duration = self._pool_mean_temperature / 2

        return super().duration


class AbacusFilteringDuration(FilteringDuration):
    """Advanced calculation method using an abacus.
    D = a*T^3 + b*T^2 + c*T +d
    T is forced at a 10°C minimum
    
    
    Formula discovered here: https://github.com/scadinot/pool
    """

    @property
    def duration(self) -> float:
        """Filtering duration in hours"""
        # Force temperature at a 10°C minimum to ensure minimum filtration.
        temperature = max(self._pool_mean_temperature, 10)

        self._computed_filtering_duration = (
            0.00335 * temperature ** 3
            - 0.14953 * temperature ** 2
            + 2.43489 * temperature
            - 10.72859
        )

        return super().duration


# TODO: caractéristique pompe.
# TODO: ajouter modificateur nombre de personne.
