# ==============================================================================
#  This file contains the main windowing code for SE
# ==============================================================================


"""
SE - planet.py

Created by Peter May on 2015-02-19.

This file contains the initial code for a planet

written by -        Peter May a-pemay@microsoft.com

"""

# local imports
import colony
import segment


class Planet(segment.Segment):
    def __init__(self, i_name='Earth'):
        """
        :param i_name: the name of the planet
        :type i_name: string
        """
        super(Planet, self).__init__(i_type='planet')
        # variables
        self.m_terrain = 'terra'
        self.m_colony = None
        self.m_sizeSupport = 3
        self.m_name = i_name

    def colonize(self, i_level, i_pop_boost):
        if self.m_colony is None:
            self.m_colony = colony.Colony(i_population=i_pop_boost, i_level=i_level)
        elif i_level > self.m_sizeSupport:
            self.m_colony.colonize(i_pop_boost, self.m_sizeSupport)
        else:
            self.m_colony.colonize(i_pop_boost, i_level)