# coding: utf-8
"""pypool_pump package allows to compute the duration of the swiming pool
filtering.
"""

from .__version__ import __version__, VERSION


class FilteringDuration(object):
    """Root class with common parts"""

    def __init__(self, percentage: float = None):
        self._computed_filtering_duration = None
        self._modifier_pecentage = percentage

    def duration(self) -> float:
        """Filtering duration in hours
        
        If modifier have been set, they will be applied to the computed filtering
        duration.
        Maximum duration is always 24 hours.
        """
        consolidated_duration = max(min(self._computed_filtering_duration, 24), 0)
        if self._modifier_pecentage is None:
            return consolidated_duration
        else:
            return consolidated_duration * self._modifier_pecentage / 100


class DumbFilteringDuration(FilteringDuration):
    """Dumb duration calulation method with taking temperature/2"""

    def duration(self, pool_temperature: float) -> float:
        """Filtering duration in hours"""
        self._computed_filtering_duration = pool_temperature / 2

        return super().duration()


class BasicFilteringDuration(FilteringDuration):
    """Basic duration calculation method with:
    - 0 below 10°C
    - temperature/3 between 10°C and 14°C
    - temperature/2 between 14°C and 30°C
    - continuous filtration above 30°C
    """

    def duration(self, pool_temperature: float) -> float:
        """Filtering duration in hours"""
        if pool_temperature < 10:
            # No need to filter below 10°C.
            self._computed_filtering_duration = 0
        elif pool_temperature < 14:
            # between 10 and 14 we can reduce filtering
            self._computed_filtering_duration = pool_temperature / 3
        elif pool_temperature >= 30:
            # Above 30°C it is recommanded to filter continuously.
            self._computed_filtering_duration = 24
        else:
            self._computed_filtering_duration = pool_temperature / 2

        return super().duration()


class AbacusFilteringDuration(FilteringDuration):
    """Advanced calculation method using an abacus.
    D = a*T^3 + b*T^2 + c*T +d
    T is forced at a 10°C minimum
    
    
    Formula discovered here: https://github.com/scadinot/pool
    """

    def duration(self, pool_temperature: float) -> float:
        """Filtering duration in hours"""
        # Force temperature at a 10°C minimum to ensure minimum filtration.
        temperature = max(pool_temperature, 10)

        self._computed_filtering_duration = (
            0.00335 * temperature ** 3
            - 0.14953 * temperature ** 2
            + 2.43489 * temperature
            - 10.72859
        )

        return super().duration()


class PumpCaracteristicFilteringDuration(FilteringDuration):
    """Advanced calculatin method using the caracteristic of your water pump and your 
    pool.
    """

    def __init__(self, pool_volume: float, pump_flow: float, percentage: float = None):
        self.pool_volume = pool_volume
        self.pump_flow = pump_flow
        super().__init__(percentage)

    def duration(
        self, pool_temperature: float, number_of_bathers: float = None
    ) -> float:
        """Filtering duration in hours"""
        cycle_duration = self.pool_volume / self.pump_flow

        if pool_temperature > 25:
            self._computed_filtering_duration = 3 * cycle_duration
            # TODO: +2 hours if > 28°c ?
        elif pool_temperature > 20:
            self._computed_filtering_duration = 2 * cycle_duration
        elif pool_temperature > 15:
            self._computed_filtering_duration = 1 * cycle_duration
        elif pool_temperature > 10:
            self._computed_filtering_duration = 0.5 * cycle_duration
        else:
            self._computed_filtering_duration = 0

        if number_of_bathers is not None:
            bather_modifier = number_of_bathers / self.pump_flow * 2
            self._computed_filtering_duration = (
                self._computed_filtering_duration + bather_modifier
            )

        return super().duration()


# TODO: caractéristique pompe.
# TODO: ajouter modificateur nombre de personne.
# TODO: ajouter modificateur pour temps lours ou orageux
