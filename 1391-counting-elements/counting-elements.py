from collections import Counter

class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = Counter(arr)
        res = 0

        for i in arr:
            if i + 1 in count:
                res += 1
        
        return res