from collections import Counter

class Solution:
    # O(nlogn), O(k)
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_s = sorted(count, key=count.get, reverse=True)

        res = []
        for i in sorted_s:
            res.append(i * count[i])

        return ''.join(res)