# Last updated: 8/17/2025, 7:50:56 PM
from collections import Counter

class Solution:
    # O(n), O(n+m)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Early termination
        if len(ransomNote) > len(magazine):
            return False

        m_counter = Counter(magazine)

        for char in ransomNote:
            m_counter[char] -= 1
            if m_counter[char] < 0:
                return False

        return True