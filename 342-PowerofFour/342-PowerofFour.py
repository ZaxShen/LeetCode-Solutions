# Last updated: 8/15/2025, 3:53:10 PM
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True

        exp = 1
        curr = 4
        while curr <= n:
            curr = 4 ** exp
            exp += 1
            if curr == n:
                return True
        
        return False