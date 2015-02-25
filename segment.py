# ==============================================================================
#  This file contains the segment base class...this is used for empty segments
#  and specific segments inherit from it
# ==============================================================================


"""
SE - planet.py

Created by Peter May on 2015-02-25.

This file contains the initial code for a segment

written by -        Peter May a-pemay@microsoft.com

"""


class Segment():
    def __init__(self, i_type='empty'):
        """
        :param i_type: the type of segment
        :type i_type: string
        """
        # variables
        self.m_type = i_type

    @property
    def type(self):
        return self.m_type