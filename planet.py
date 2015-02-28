# ==============================================================================
#  This file contains the main code for a planet, which inherits from Segment,
#  and adds support for a colony, naming and terrain
# ==============================================================================


"""
SE - Planet.py

Created by Peter May on 2015-02-19.

written by -        Peter May a-pemay@microsoft.com

"""

# local imports
import Colony
import Segment


class Planet(Segment.Segment):
    # ==============================================================================
    # Initialisation
    # ==============================================================================
    def __init__(self, i_name='Earth'):
        """
        initialise the planet
        :param i_name: the name of the planet
        :type i_name: string
        """
        super(Planet, self).__init__(i_type='planet')
        # variables
        self.m_terrain = 'terra'
        self.m_colony = Colony.Colony(i_population=0, i_level=0)
        self.m_sizeSupport = 3
        self.m_name = i_name

    # ==============================================================================
    # Behaviour
    # ==============================================================================
    def colonize(self, i_level, i_pop_boost):
        """
        colonize the planet, either add to an existing colony or make a new one
        :type i_level: int
        :type i_pop_boost: int
        :param i_level:
        :param i_pop_boost:
        """
        # if the input level is greater than the level supported by the planet, clamp it
        if i_level > self.m_sizeSupport:
            self.m_colony.colonize(i_pop_boost, self.m_sizeSupport)

        # otherwise just do the colonisation
        else:
            self.m_colony.colonize(i_pop_boost, i_level)

    def simulate(self):
        """
        run the simulation on the planet
        """
        self.m_colony.simulate()

    # ==============================================================================
    #  Properties
    # ==============================================================================
    @property
    def colony(self):
        """
        :return: self.m_colony - the colony on the planet
        :rtype : Colony
        """
        return self.m_colony