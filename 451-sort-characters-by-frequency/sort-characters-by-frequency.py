from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)

        sorted_count = sorted(count, key=count.get, reverse=True)

        res = []
        for char in sorted_count:
            res.append(char * count[char])

        return ''.join(res)