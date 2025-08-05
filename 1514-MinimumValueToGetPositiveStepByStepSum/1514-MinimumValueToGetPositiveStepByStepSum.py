# Last updated: 8/4/2025, 10:45:24 PM
class Solution:
    # O(n), O(1)
    def minStartValue(self, nums: list[int]) -> int:
        acc =  0
        min_acc = 0

        for i in range(len(nums)):
            acc += nums[i]
            min_acc = min(min_acc, acc)

        return -min_acc + 1