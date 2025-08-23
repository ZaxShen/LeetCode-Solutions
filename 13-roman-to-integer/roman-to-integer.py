class Solution:
    # O(n), O(1)
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
            curr_num, next_num = roman[s[i]], roman[s[i + 1]]
            if curr_num >= next_num:
                res += curr_num
            else:
                res -= curr_num

        # Add the final num
        res += roman[s[-1]]

        return res
