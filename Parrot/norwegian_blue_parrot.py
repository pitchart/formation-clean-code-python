from parrot import Parrot


class NorwegianBlueParrot(Parrot):
    def __init__(self, voltage, nailed):
        self.voltage = voltage
        self.nailed = nailed
        self.base_speed = 12

    def _compute_base_speed_for_voltage(self):
        return min([24.0, self.voltage * self.base_speed])

    def speed(self):
        if self.nailed:
            return 0
        else:
            return self._compute_base_speed_for_voltage()
