from collections import Counter

class Solution:
    # O(nlogn), O(k)
    def frequencySort(self, s: str) -> str:
        count = Counter(s)

        sorted_s = sorted(count, key=count.get, reverse=True)

        res = ''
        for k in sorted_s:
            res += k * count[k]

        return res