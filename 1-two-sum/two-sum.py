class Solution:
    # O(n), O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in d:
                return [d[diff], i]
            d[num] = i

        return [-1, -1]