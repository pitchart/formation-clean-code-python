from unittest import TestCase

from african_parrot import AfricanParrot
from european_parrot import EuropeanParrot
from norwegian_blue_parrot import NorwegianBlueParrot


class EuropeanParrotTest(TestCase):

    def test_speedOfEuropeanParrot(self) -> None:
        parrot = EuropeanParrot()
        self.assertEqual(12.0, parrot.speed())


class AfricanParrotTest(TestCase):
    def test_speedOfAfricanParrot_With_One_Coconut(self):
        parrot = AfricanParrot(1)
        self.assertEqual(3.0, parrot.speed())

    def test_speedOfAfricanParrot_With_Two_Coconuts(self):
        parrot = AfricanParrot(2)
        self.assertEqual(0.0, parrot.speed())

    def test_speedOfAfricanParrot_With_No_Coconuts(self):
        parrot = AfricanParrot(0)
        self.assertEqual(12.0, parrot.speed())


class ParrotTest(TestCase):

    def test_speedNorwegianBlueParrot_nailed(self):
        parrot = NorwegianBlueParrot(1.5, True)
        self.assertEqual(0.0, parrot.speed())

    def test_speedNorwegianBlueParrot_not_nailed(self):
        parrot = NorwegianBlueParrot(1.5, False)
        self.assertEqual(18.0, parrot.speed())

    def test_speedNorwegianBlueParrot_not_nailed_high_voltage(self):
        parrot = NorwegianBlueParrot(4, False)
        self.assertEqual(24.0, parrot.speed())
