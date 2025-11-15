from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote): return False

        count = Counter(magazine)

        for i in ransomNote:
            if i not in count:
                return False
            else:
                if count[i] <= 0:
                    return False
                count[i] -= 1

        return True