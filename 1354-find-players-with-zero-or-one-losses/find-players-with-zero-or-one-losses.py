from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = Counter()
        losers = Counter()

        for winner, loser in matches:
            winners[winner] += 1
            losers[loser] += 1

        zero_lose = winners.keys() - losers.keys()
        one_lose = []

        for k, v in losers.items():
            if v == 1:
                one_lose.append(k)

        return sorted(zero_lose), sorted(one_lose)