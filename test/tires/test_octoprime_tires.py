import unittest
from datetime import datetime
from tires.models.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):

    def test_tires_needs_service_true(self):
        tire_wear = [1, 1, 0.9, 0.2]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_tires_needs_service_false(self):
        tire_wear = [1, 0.5, 0.5, 0.5]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())


if __name__ == '__main__':
    unittest.main()
