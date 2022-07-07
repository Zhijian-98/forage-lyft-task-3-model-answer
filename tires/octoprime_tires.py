from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, nums):
        self.nums = nums
    
    def needs_service(self):
        sum = 0
        for num in self.nums:
            sum += num
        if sum >= 3:
            return True
        else:
            return False