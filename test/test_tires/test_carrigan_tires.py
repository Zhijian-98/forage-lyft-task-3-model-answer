import unittest

from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def needs_service_true(self):
        nums = [0.1, 0.5, 0.9, 0.8]
        tires = CarriganTires(nums)
        self.assertTrue(tires.needs_service())
    
    def needs_service_false(self):
        nums = [0.1, 0.5, 0.6, 0.4]
        tires = CarriganTires(nums)
        self.assertFalse(tires.needs_service())