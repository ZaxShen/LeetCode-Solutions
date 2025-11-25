from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False

        count = Counter(magazine)

        for i in ransomNote:
            count[i] -= 1
            if count[i] < 0:
                return False

        return True