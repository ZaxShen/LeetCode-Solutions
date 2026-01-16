from collections import Counter

class Solution:
    # O(n), O(k)
    def countElements(self, arr: List[int]) -> int:
        count = Counter(arr)
        res = 0

        for k, v in count.items():
            if k + 1 in count:
                res += v
        
        return res

