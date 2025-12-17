class Solution:
    # O(n), O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, i in enumerate(nums):
            diff = target - i
            if diff in seen:
                return [seen[diff], idx]
            seen[i] = idx
            
        return [-1, -1]