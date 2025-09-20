class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        prefix = 0
        for i in range(len(s) - 1):
            n1, n2 = roman[s[i]], roman[s[i + 1]]
            if n1 < n2:
                prefix -= n1
            else:
                prefix += n1

        prefix += roman[s[-1]]

        return prefix

