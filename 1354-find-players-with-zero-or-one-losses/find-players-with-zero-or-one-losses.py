from collections import Counter

class Solution:
    # O(nlogn), O(k)
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = Counter()
        losers = Counter()

        for winner, loser in matches:
            winners[winner] += 1
            losers[loser] += 1

        zero_loss = winners.keys() - losers.keys()
        one_loss = [k for k,v in losers.items() if v == 1]

        return sorted(zero_loss), sorted(one_loss)