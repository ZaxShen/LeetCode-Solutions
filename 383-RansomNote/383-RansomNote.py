# Last updated: 8/17/2025, 7:47:53 PM
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_counter = Counter(ransomNote)
        m_counter = Counter(magazine)

        for char, count in r_counter.items():
            if count > m_counter[char]:
                return False

        return True