class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge Case
        if len(strs) == 1: return strs[0]

        min_len = min([len(i) for i in strs])

        for i in range(min_len):
            char = strs[0][i]
            for word in strs[1:]:
                if word[i] != char:
                    return strs[0][:i]

        return strs[0][:min_len]