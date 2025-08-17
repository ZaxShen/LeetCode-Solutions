# Last updated: 8/17/2025, 7:48:31 PM
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Early termination
        if len(ransomNote) > len(magazine):
            return False

        r_counter = Counter(ransomNote)
        m_counter = Counter(magazine)

        for char, count in r_counter.items():
            if count > m_counter[char]:
                return False

        return True