# Last updated: 8/17/2025, 12:16:55 AM
from collections import Counter

class Solution:
    # O(nlogn), O(n)
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses_count = Counter()

        for winner, loser in matches:
            losses_count[winner] = losses_count.get(winner, 0)
            losses_count[loser] += 1

        zero_loss, one_loss = [], []
        for player, loss in losses_count.items():
            if loss == 0:
                zero_loss.append(player)
            elif loss == 1:
                one_loss.append(player)

        return sorted(zero_loss), sorted(one_loss)
