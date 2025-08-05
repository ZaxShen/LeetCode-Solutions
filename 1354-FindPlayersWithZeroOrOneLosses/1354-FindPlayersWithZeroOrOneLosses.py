# Last updated: 8/4/2025, 10:45:43 PM
class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losses_count = {}

        for w, l in matches:
            losses_count[w] = losses_count.get(w, 0)
            losses_count[l] = losses_count.get(l, 0) + 1

        zero_loss, one_loss = [], []
        for player, count in losses_count.items():
            if count == 0:
                zero_loss.append(player)
            elif count == 1:
                one_loss.append(player)

        return [sorted(zero_loss), sorted(one_loss)]