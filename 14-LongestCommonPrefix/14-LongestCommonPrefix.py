# Last updated: 8/13/2025, 1:13:13 AM
class Solution:
    # O()
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            char = strs[0][i]

            for s in strs[1:]:
                if char != s[i]:
                    return s[:i]

        return strs[0][:min_len]
