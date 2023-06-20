from enum import Enum


class ParrotType(Enum):  # If it is not available, just remove it.
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class Parrot:

    def __init__(self, type_of_parrot, number_of_coconuts, voltage, nailed):
        self._type = type_of_parrot
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    def speed(self):
        raise ValueError("should be unreachable")

    def _load_factor(self):
        return 9.0

    def _base_speed(self):
        return 12.0

    @classmethod
    def create(cls, type_of_parrot, number_of_coconuts, voltage, nailed):
        if type_of_parrot == ParrotType.EUROPEAN:
            return cls()
        if type_of_parrot == ParrotType.AFRICAN:
            return cls(number_of_coconuts=number_of_coconuts)
        if type_of_parrot == ParrotType.NORWEGIAN_BLUE:
            return cls(voltage=voltage, nailed=nailed)
        return cls(type_of_parrot, number_of_coconuts, voltage, nailed)
