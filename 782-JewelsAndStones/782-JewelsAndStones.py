# Last updated: 8/4/2025, 10:46:39 PM
class Solution:
    # O(n), O(k)
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j_set = set(jewels)
        
        return sum(s in j_set for s in stones)