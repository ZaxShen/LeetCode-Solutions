from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Edge Case
        if len(ransomNote) > len(magazine): return False

        return Counter(ransomNote) <= Counter(magazine)