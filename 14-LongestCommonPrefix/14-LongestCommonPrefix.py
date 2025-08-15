# Last updated: 8/15/2025, 5:14:05 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            char = strs[0][i]
            for s in strs[1:]:
                if s[i] != char:
                    return s[:i]

        return strs[0][:min_len]