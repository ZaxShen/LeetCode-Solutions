class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stone in set(jewels) for stone in stones)

