

from parrot import Parrot


class AfricanParrot(Parrot):
    def __init__(self, number_of_coconuts):
        self.number_of_coconuts = number_of_coconuts
        self.base_speed = 12
        self.load_factor = 9
    
    def speed(self):
        return max(0, self.base_speed - self.load_factor * self.number_of_coconuts)