from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = Counter()

        for winner, loser in matches:
            loss_count[winner] += 0
            loss_count[loser] += 1

        zero_loss, one_loss = [], []
        for k, v in loss_count.items():
            if v == 0: zero_loss.append(k)
            elif v == 1: one_loss.append(k)

        return sorted(zero_loss), sorted(one_loss)