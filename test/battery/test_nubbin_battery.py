import unittest
from datetime import datetime
from battery.models.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):

    def test_battery_needs_service_true1(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_battery_needs_service_true2(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_battery_needs_service_false1(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

    def test_battery_needs_service_false2(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 0)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
