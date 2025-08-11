# Last updated: 8/11/2025, 7:24:33 PM
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        current_cost = left = 0
        
        for right in range(len(s)):
            current_cost += abs(ord(s[right]) - ord(t[right]))
            
            # If invalid, move left pointer once (maintain max window size)
            if current_cost > maxCost:
                current_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
        
        return right - left + 1