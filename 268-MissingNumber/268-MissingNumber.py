# Last updated: 8/14/2025, 1:34:27 AM
class Solution:
    # O(n), O(n)
    def missingNumber(self, nums: List[int]) -> int:
        uni_nums = set(range(len(nums) + 1))

        return list(uni_nums - set(nums))[0]