# Last updated: 8/17/2025, 8:04:56 PM
class Solution:
    # O(n+m), O(m)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Early termination
        if len(ransomNote) > len(magazine):
            return False

        m_counter = {}
        for char in magazine:
            m_counter[char] = m_counter.get(char, 0) + 1

        for char in ransomNote:
            if m_counter.get(char, 0) == 0:
                return False
            m_counter[char] -= 1

        return True