from GameFrame import BlueBot, Globals
from enum import Enum


class STATE(Enum):
    WAIT = 1
    ATTACK = 2
    JAIL_BREAK = 3


class Blue1(BlueBot):
    def __init__(self, room, x, y):
        BlueBot.__init__(self, room, x, y)

        self.curr_state = STATE.WAIT

    def tick(self):
        pass
  
