# Last updated: 8/4/2025, 10:43:38 PM
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        min_len = float('inf')
        d = {}

        for i, card in enumerate(cards):
            if card in d:
                min_len = min(min_len, i - d[card])
            d[card] = i

        if min_len != float('inf'):
            return min_len + 1
        return -1