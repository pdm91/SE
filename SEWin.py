# ==============================================================================
#  This file contains the main windowing code for SE
# ==============================================================================


"""
SE - SEWin.py

Created by Peter May on 2015-02-19.

This file contains the main windowing code for SE

written by -        Peter May a-pemay@microsoft.com

"""

# local imports
import Planet

# libraries
import pyglet


class SEWindow(pyglet.window.Window):
    def __init__(self):
        super(SEWindow, self).__init__(caption='Space Empires...ish')

        self.m_label = pyglet.text.Label('Space Empires...ish')
        self.m_planet = Planet.Planet(i_name='earth')
        self.m_level = 1

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.C:
            self.m_planet.colonize(self.m_level, 10000)
            self.m_level += 1

        if symbol == pyglet.window.key.S:
            self.m_planet.m_colony.simulate()

        self.m_label.text = 'Planet: '+self.m_planet.m_name+' '+str(self.m_planet.m_colony.population)+' Level: '+str(self.m_planet.m_colony.level)
        self.on_draw()

    def on_draw(self):
        self.clear()
        self.m_label.draw()

if __name__ == '__main__':
    window = SEWindow()
    pyglet.app.run()