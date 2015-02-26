# ==============================================================================
# This file contains the main code for a galaxy, a collection of space segments,
# some of which maybe habitable
# ==============================================================================

"""
SE - galaxy.py

Created by Peter May on 2015-02-19.

written by -        Peter May a-pemay@microsoft.com

"""

# local imports
import planet
import segment

# global python imports
import random


class Galaxy():
    # ==============================================================================
    # Initialisation
    # ==============================================================================
    def __init__(self, i_name='Milky Way', i_size=10):
        """
        initialise the galaxy
        :param i_name: the name of the galaxy
        :type i_name: str
        :param i_size: the number of sections across the sides of the galaxy
        :type i_size: int
        """
        self.m_size = i_size
        self.m_name = i_name
        self.m_grid = self.make_grid()
        self.m_planets = self.get_planets()

    def make_grid(self):
        """
        make a grid for the galaxy
        :rtype : list[list[Segment]]
        :return: grid, a 2D list of galaxy segments, some of which will be planets
        """

        # initialise the grid
        grid = []

        # cycle through for each column
        for i in range(0, self.m_size):
            # then cycle through for each element, currently only supports square galaxies
            column = []
            for j in range(0, self.m_size):
                # randomly determine whether or not to make a planet, if not just make an empty
                # segment
                if random.randint(0, 100) < 10:
                    column.append(planet.Planet(i_name=('earth'+str(i+j))))
                else:
                    column.append(segment.Segment())
            grid.append(column)
        # finally return the grid
        return grid

    def get_planets(self):
        """
        get a list of the planets
        :rtype : list[Planet]
        :return: planets, a list of the planets in the galaxy
        """
        # initialise the list
        planets = []

        # cycle through for each column
        for i in range(0, self.m_size):
            # then cycle through for each element, currently only supports square galaxies
            for j in range(0, self.m_size):
                # if the type is planet
                if self.m_grid[i][j].Segment.type == 'planet':
                    # add it to the list
                    planets.append(self.m_grid[i][j])
        # and return
        return planets