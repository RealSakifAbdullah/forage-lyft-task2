import unittest
from datetime import datetime
from tires.models.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):

    def test_tires_needs_service_true(self):
        tire_wear = [0, 0, 0.9, 0]
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_tires_needs_service_false(self):
        tire_wear = [0.5, 0, 0, 0]
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())


if __name__ == '__main__':
    unittest.main()
