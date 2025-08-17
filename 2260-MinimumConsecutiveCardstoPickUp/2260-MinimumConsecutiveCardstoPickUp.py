# Last updated: 8/17/2025, 6:05:48 PM
from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        card_pos = defaultdict(list)

        res = float('inf')
        for i, card in enumerate(cards):
            if card in card_pos:
                res = min(res, i - card_pos[card][-1] + 1)
            card_pos[card].append(i)

        return res if res != float('inf') else -1
