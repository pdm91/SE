# ==============================================================================
#  This file contains the segment base class...this is used for empty segments
#  and specific segments inherit from it
# ==============================================================================


"""
SE - segment.py

Created by Peter May on 2015-02-25.

written by -        Peter May a-pemay@microsoft.com

"""


class Segment():
    # ==============================================================================
    # Initialisation
    # ==============================================================================
    def __init__(self, i_type='empty'):
        """
        initialise the segment
        :param i_type: the type of segment
        :type i_type: string
        """
        # variables
        self.m_type = i_type

    # ==============================================================================
    #  Properties
    # ==============================================================================
    @property
    def type(self):
        """
        :return: self.m_type - the type of segment that this is
        :rtype : str
        """
        return self.m_type