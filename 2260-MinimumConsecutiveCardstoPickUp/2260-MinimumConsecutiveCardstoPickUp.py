# Last updated: 8/17/2025, 6:07:35 PM
class Solution:
    # O(n), O(m)
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen ={}

        res = float('inf')
        for i, card in enumerate(cards):
            if card in seen:
                res = min(res, i - seen[card] + 1)
            seen[card] = i

        return res if res != float('inf') else -1
