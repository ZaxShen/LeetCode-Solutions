# Last updated: 8/10/2025, 10:38:47 PM
class Solution:
    # O(n), O(1)
    def minStartValue(self, nums: List[int]) -> int:
        curr = min_acc = 0
        for num in nums:
            curr += num
            min_acc = min(min_acc, curr)

        return -min_acc + 1