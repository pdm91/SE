# ==============================================================================
#  This file contains the main windowing code for SE
# ==============================================================================


"""
SE - SEWin.py

Created by Peter May on 2015-02-19.

This file contains the main windowing code for SE

written by -        Peter May a-pemay@microsoft.com

"""

import pyglet


class SEWindow(pyglet.window.Window):
    def __init__(self):
        super(SEWindow, self).__init__(caption='Space Empires...ish')

        self.label = pyglet.text.Label('Space Empires...ish')

    def on_draw(self):
        self.clear()
        self.label.draw()

if __name__ == '__main__':
    window = SEWindow()
    pyglet.app.run()