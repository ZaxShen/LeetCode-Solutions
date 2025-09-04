from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)

        return set(count.values()) != {1}