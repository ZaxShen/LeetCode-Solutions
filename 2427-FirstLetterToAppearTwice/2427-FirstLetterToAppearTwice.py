# Last updated: 8/4/2025, 10:43:35 PM
class Solution:
    # O(n), O(m)
    def repeatedCharacter(self, s: str) -> str:
        unique_s = set()
        
        for i in s:
            if i in unique_s:
                return i
            unique_s.add(i)