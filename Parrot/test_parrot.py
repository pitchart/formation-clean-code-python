from african_parrot import AfricanParrot
from norwegian_blue_parrot import NorwegianBlueParrot
from parrot import Parrot, ParrotType
from european_parrot import EuropeanParrot
from unittest import TestCase


class EuropeanParrotTest(TestCase):

    def test_speedOfEuropeanParrot(self) -> None:
        parrot = EuropeanParrot.create(ParrotType.EUROPEAN, 0, 0, False)
        self.assertEqual(12.0, parrot.speed())


class AfricanParrotTest(TestCase):
    def test_speedOfAfricanParrot_With_One_Coconut(self):
        parrot = AfricanParrot.create(ParrotType.AFRICAN, 1, 0, False)
        self.assertEqual(3.0, parrot.speed())

    def test_speedOfAfricanParrot_With_Two_Coconuts(self):
        parrot = AfricanParrot.create(ParrotType.AFRICAN, 2, 0, False)
        self.assertEqual(0.0, parrot.speed())

    def test_speedOfAfricanParrot_With_No_Coconuts(self):
        parrot = AfricanParrot.create(ParrotType.AFRICAN, 0, 0, False)
        self.assertEqual(12.0, parrot.speed())


class ParrotTest(TestCase):

    def test_speedNorwegianBlueParrot_nailed(self):
        parrot = NorwegianBlueParrot.create(ParrotType.NORWEGIAN_BLUE, 0, 1.5, True)
        self.assertEqual(0.0, parrot.speed())

    def test_speedNorwegianBlueParrot_not_nailed(self):
        parrot = NorwegianBlueParrot.create(ParrotType.NORWEGIAN_BLUE, 0, 1.5, False)
        self.assertEqual(18.0, parrot.speed())

    def test_speedNorwegianBlueParrot_not_nailed_high_voltage(self):
        parrot = NorwegianBlueParrot.create(ParrotType.NORWEGIAN_BLUE, 0, 4, False)
        self.assertEqual(24.0, parrot.speed())
