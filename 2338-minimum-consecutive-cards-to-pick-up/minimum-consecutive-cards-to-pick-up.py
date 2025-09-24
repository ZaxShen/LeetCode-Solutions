from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen = defaultdict(int)
        res = float("inf")

        for i, card in enumerate(cards):
            if card in seen:
                res = min(res, i - seen[card] + 1)

            seen[card] = i

        return res if res != float("inf") else -1