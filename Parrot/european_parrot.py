from parrot import Parrot, ParrotType


class EuropeanParrot(Parrot):

    def __init__(self):
        super().__init__(type_of_parrot=ParrotType.EUROPEAN, number_of_coconuts=0, voltage=0, nailed=False)
        self.base_speed: int = 12

    def speed(self):
        return self.base_speed

