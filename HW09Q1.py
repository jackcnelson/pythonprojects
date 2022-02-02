# MIS 207
#
#

class Lamp:

    def __init__(self):
        self._lamp_on = False

    def flip_switch(self):
        if self._lamp_on:
            self._lamp_on = False
        else:
            self._lamp_on = True

    def lamp_state(self):
        if not self._lamp_on:
            return 'The lamp is off'
        else:
            return 'The lamp is on'
