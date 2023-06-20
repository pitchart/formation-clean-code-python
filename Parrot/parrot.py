from abc import ABC, abstractmethod


class Parrot(ABC):

    @abstractmethod
    def speed(self):
        pass

