# Last updated: 8/14/2025, 3:19:41 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(word) for word in strs)
        res = []

        for i in range(min_len):
            char = strs[0][i]
            for j in strs[1:]:
                if j[i] != char:
                    return j[:i]
            res.append(char)

        return ''.join(res)