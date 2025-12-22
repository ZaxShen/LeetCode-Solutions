from collections import Counter

class Solution:
    # O(n), O(k)
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        res = []

        for k, v in count.most_common():
            res.append(k * v)

        return ''.join(res)