# Last updated: 8/16/2025, 1:10:40 PM
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))

        try:
            first_6 = num.index('6')
            num[first_6] = '9'
        finally:
            return int(''.join(num))