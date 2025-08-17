# Last updated: 8/16/2025, 11:10:56 PM
from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)

        res = min(
            counter['b'],
            counter['a'],
            counter['l'] // 2,
            counter['o'] // 2,
            counter['n']
            )

        return res
