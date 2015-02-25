"""
SE - galaxy.py

Created by Peter May on 2015-02-19.

This file contains the initial code for a galaxy

written by -        Peter May a-pemay@microsoft.com

"""

import planet


class Galaxy():
    # ==============================================================================
    # Initialisation
    # ==============================================================================
    def __init__(self, i_name='Milky Way', i_size=10):
        self.m_size = i_size
        self.m_name = i_name
        self.m_grid = self.make_grid()
        self.m_planets = self.get_planets(self.m_grid)

    def make_grid(self):

        return grid