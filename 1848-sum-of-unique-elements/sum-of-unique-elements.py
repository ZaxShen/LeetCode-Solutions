from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter()

        res = 0
        for num in nums:
            count[num] += 1
            if count[num] == 1:
                res += num
            elif count[num] == 2:
                res -= num

        return res
            