# Last updated: 8/16/2025, 12:40:50 PM
from collections import Counter

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        counter = Counter()

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                return s[i]
            else:
                if counter[s[i]] == 1:
                    return s[i]
            counter[s[i]] += 1

        return s[-1]

        