from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False

        counter = Counter(magazine)
        for i in ransomNote:
            if counter[i] == 0:
                return False
            counter[i] -= 1

        return True