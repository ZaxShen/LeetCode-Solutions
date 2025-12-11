class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(strs[0])
        for i in strs: min_len = min(min_len, len(i))

        for i in range(min_len):
            word = strs[0][i]
            for j in strs[1:]:
                if word != j[i]:
                    return ''.join(strs[0][:i])

        return ''.join(strs[0][:min_len])
                