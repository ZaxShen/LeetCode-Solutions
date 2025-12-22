from collections import Counter

class Solution:
    # O(n), O(k)
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter()
        res = 0

        for i in nums:
            count[i] += 1

            if count[i] == 1:
                res += i
            elif count[i] == 2:
                res -= i

        return res