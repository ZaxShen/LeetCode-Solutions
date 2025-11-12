class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        res = 0
        for i in stones:
            if i in jewels:
                res += 1

        return res