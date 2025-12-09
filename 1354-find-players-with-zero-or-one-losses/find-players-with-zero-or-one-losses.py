from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = Counter()
        losers = Counter()

        for winner, loser in matches:
            winners[winner] += 1
            losers[loser] += 1

        zero_lose = winners.keys() - losers.keys()
        one_lose = [loser for loser, matches in losers.items() if matches == 1]
        return sorted(zero_lose), sorted(one_lose)