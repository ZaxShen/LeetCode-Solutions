from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen = defaultdict(int)
        res = float('inf')

        for idx, i in enumerate(cards):
            if i in seen:
                res = min(res, idx - seen[i] + 1)
            seen[i] = idx

        return res if res != float('inf') else -1
