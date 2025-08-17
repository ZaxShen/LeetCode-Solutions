# Last updated: 8/17/2025, 12:04:26 AM
from collections import Counter

class Solution:
    # O(nlogn), O(n)
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = Counter()
        losers = Counter()

        for winner, loser in matches:
            winners[winner] += 1
            losers[loser] += 1
        
        zero_loss = set(winners.keys() - losers.keys())
        one_loss = [loser for loser in losers if losers[loser] == 1]

        return sorted(zero_loss), sorted(one_loss)
            


