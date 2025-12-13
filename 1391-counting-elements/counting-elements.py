from collections import Counter

class Solution:
    def countElements(self, arr: List[int]) -> int:
        res = 0
        count = Counter(arr)

        for i in count:
            if i + 1 in count:
                res += count[i]

        return res