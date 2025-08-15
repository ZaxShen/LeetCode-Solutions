# Last updated: 8/14/2025, 11:39:50 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)
        count = 0

        for i in range(min_len):
            char = strs[0][i]

            for s in strs[1:]:
                if s[i] != char:
                    return s[:i]

        return strs[0][:min_len]



