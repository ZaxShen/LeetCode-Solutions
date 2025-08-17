# Last updated: 8/17/2025, 12:52:56 PM
from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = Counter()

        for winner, loser in matches:
            loss_count[winner] += 0
            loss_count[loser] += 1

        zero_loss = []
        one_loss = []
        for player, loss in loss_count.items():
            if loss == 0:
                zero_loss.append(player)
            elif loss == 1:
                one_loss.append(player)

        return sorted(zero_loss), sorted(one_loss)