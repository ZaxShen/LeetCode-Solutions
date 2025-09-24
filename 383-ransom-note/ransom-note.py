from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        count = Counter(magazine)
        for char in ransomNote:
            count[char] -= 1
            if count[char] < 0:
                return False

        return True