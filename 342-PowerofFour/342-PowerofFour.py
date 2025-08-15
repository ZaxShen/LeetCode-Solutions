# Last updated: 8/15/2025, 3:55:13 PM
from math import log2

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log2(n) % 2 == 0