class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0
        for i in range(len(s) - 1):
            num, _ = roman[s[i]], roman[s[i + 1]]
            if num >= _:
                res += num
            else:
                res -= num

        # Add final num
        res += roman[s[-1]]

        return res
