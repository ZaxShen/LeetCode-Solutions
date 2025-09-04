from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = Counter()
        losers = Counter()
        
        for winner, loser in matches:
            winners[winner] += 1
            losers[loser] += 1

        zero_lose = set(winners.keys() - losers.keys())
        one_lose = [loser for loser, count in losers.items() if count == 1]

        return sorted(zero_lose), sorted(one_lose)

        