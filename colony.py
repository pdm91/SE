# ==============================================================================
#  This file contains the main windowing code for SE
# ==============================================================================


"""
SE - colony.py

Created by Peter May on 2015-02-19.

This file contains the initial code for a planet

written by -        Peter May a-pemay@microsoft.com

"""


class Colony():
    # ==============================================================================
    #  Initialisation
    # ==============================================================================
    def __init__(self, i_population=0, i_level=1):

        """
        initialise the colony with a population and a level
        :param i_population:    the population of the colony
        :param i_level:         the colony level (outpost,colony, settlement)
        :type i_population: int
        :type i_level: int
        """
        # variables
        self.m_population = i_population
        self.m_level = i_level
        self.m_production = 0.0

    # ==============================================================================
    #  Behaviour
    # ==============================================================================
    def colonize(self, i_pop_boost, i_level):
        """
        colonize the colony - upgrade the development level and boost population
        :param i_pop_boost:
        :param i_level:
        :type i_pop_boost: int
        :type i_level: int
        """
        # increase the colony level
        if i_level > self.m_level:
            self.m_level = i_level

        # and add on the population
        self.m_population += i_pop_boost

        # set the production output
        self.m_production = float(self.m_population)/10.0

    def simulate(self):
        """
        simulate the colony, grow naturally and produce money

        """
        # increase population
        pop_fl = float(self.m_population)*1.1
        self.m_population *= int(pop_fl)

        # set the production output
        self.m_production = float(self.m_population)/10.0

    # ==============================================================================
    #  Get/Set
    # ==============================================================================
    @property
    def level(self):
        """
        :return: self.m_level
        :rtype : int
        """
        return self.m_level

    @level.setter
    def level(self, i_level):
        """
        :param i_level: the level to set the colony to
        :type i_level: int
        """
        self.m_level = i_level

    @property
    def population(self):
        return self.m_population

    @property
    def production(self):
        return self.m_production