from collections import Counter

class Solution:
    # O(n+m), O(m)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        count = Counter(magazine)
        for char in ransomNote:
            if count[char] == 0:
                return False
            count[char] -= 1

        return True