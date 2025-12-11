from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False

        c1 = Counter(ransomNote)
        c2 = Counter(magazine)

        return c2 >= c1