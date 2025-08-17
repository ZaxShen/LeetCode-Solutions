# Last updated: 8/16/2025, 11:16:05 PM
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {'a': 0, 'b': 0, 'l': 0, 'o': 0, 'n': 0}

        for c in text:
            if c in d:
                d[c] += 1

        return min(min(d['o'] // 2, d['l'] // 2), min(d.values()))