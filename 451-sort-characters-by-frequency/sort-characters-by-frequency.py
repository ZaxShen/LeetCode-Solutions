from collections import Counter

class Solution:
    # O(nlogn), O(k)
    def frequencySort(self, s: str) -> str:
        count = Counter(s)

        res = []
        for char, freq in count.most_common():
            res.append(char * freq)

        return ''.join(res)