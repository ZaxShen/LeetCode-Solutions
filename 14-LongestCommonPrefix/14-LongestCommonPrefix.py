# Last updated: 8/12/2025, 8:24:08 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Find minimum length to avoid index errors
        min_len = min(len(s) for s in strs)
        
        for i in range(min_len):
            char = strs[0][i]
            # Check if all strings have the same character at position i
            for s in strs[1:]:
                if s[i] != char:
                    return strs[0][:i]
        
        return strs[0][:min_len]