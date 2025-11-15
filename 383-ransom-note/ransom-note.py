from collections import Counter

class Solution:
    # O(m+n), O(m)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote): return False

        count = Counter(magazine)

        for i in ransomNote:
            if count[i] == 0:
                return False
            count[i] -= 1

        return True