import unittest

from tires.octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
    def needs_service_true(self):
        nums = [0.7, 0.7, 0.8, 0.8]
        tires = OctoprimeTires(nums)
        self.assertTrue(tires.needs_service())
    
    def needs_service_false(self):
        nums = [0.7, 0.6, 0.7, 0.6]
        tires = OctoprimeTires(nums)
        self.assertFalse(tires.needs_service())