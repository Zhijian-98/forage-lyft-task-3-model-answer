import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date(2020,5,15)
        last_service_date = date(2016,1,25)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date(2020,5,15)
        last_service_date = date(2019,1,10)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
