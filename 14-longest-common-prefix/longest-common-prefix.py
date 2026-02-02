class Solution:
    # O(n), O(1)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case
        if len(strs) == 1: return strs[0]

        min_len = min(map(len, strs))

        for idx in range(min_len):
            curr_char = strs[0][idx]
            for s in strs[1:]:
                if curr_char != s[idx]:
                    return strs[0][:idx]

        return strs[0][:min_len]
