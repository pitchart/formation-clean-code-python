

from parrot import Parrot, ParrotType


class AfricanParrot(Parrot):
    def __init__(self, number_of_coconuts):
        super().__init__(ParrotType.AFRICAN, number_of_coconuts, voltage=0, nailed=False)
        self.base_speed = 12
        self.load_factor = 9
    
    def speed(self):
        return max(0, self.base_speed - self.load_factor * self._number_of_coconuts)