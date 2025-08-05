# Last updated: 8/4/2025, 10:46:00 PM
class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        # F0, F1, F2, F3
        #  0,  1,  1, F3 + F2 + F1
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        return self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)