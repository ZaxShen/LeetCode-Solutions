# Last updated: 8/11/2025, 8:33:47 PM
from itertools import accumulate

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right] - self.prefix_sum[left] + self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)