from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, nums):
        self.nums = nums
    
    def needs_service(self):
        for num in self.nums:
            if num >= 0.9:
                return True
        return False
