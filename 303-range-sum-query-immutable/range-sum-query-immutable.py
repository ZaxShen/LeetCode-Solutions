from itertools import accumulate

class NumArray:

    def __init__(self, nums: List[int]):
        self.num = nums
        self.acc = tuple(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.acc[right] - self.acc[left] + self.num[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)