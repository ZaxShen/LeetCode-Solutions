class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
        prefix = 0
        self.acc = []
        for num in nums:
            prefix += num
            self.acc.append(prefix)

    def sumRange(self, left: int, right: int) -> int:
        return self.acc[right] - self.acc[left] + self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)