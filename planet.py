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


class Planet():
    def __init__(self):

        # variables
        self.m_type = "terra"
        self.m_colony = None
        self.m_sizeSupport = 3

    def colonize(self, i_level, i_pop_boost):
        if self.m_colony is None:
            self.m_colony = colony.Colony(i_population=i_pop_boost, i_level=i_level)
        else:
            self.m_colony.colonize(i_pop_boost, i_level)