class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(_) for _ in strs)


        for i in range(min_len):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return strs[0][:i]

        return strs[0][:min_len]