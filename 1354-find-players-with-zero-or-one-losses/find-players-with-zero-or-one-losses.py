from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = Counter()
        losers = Counter()

        for winner, loser in matches:
            winners[winner] += 1
            losers[loser] += 1

        res1 = [k for k in winners if k not in losers]
        res2 = [k for k, v in losers.items() if v == 1]

        return sorted(res1), sorted(res2)
