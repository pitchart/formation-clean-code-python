from parrot import Parrot


class EuropeanParrot(Parrot):

    def __init__(self):
        self.base_speed: int = 12

    def speed(self):
        return self.base_speed
