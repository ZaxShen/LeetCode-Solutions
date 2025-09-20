class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        min_len = min(len(word) for word in strs)

        for i in range(min_len):
            char = strs[0][i]
            for word in strs:
                if word[i] != char:
                    return ''.join(res)
            res.append(char)

        return ''.join(res)