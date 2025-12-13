class Solution:
    # O(n), O(n)
    def wordPattern(self, pattern: str, s: str) -> bool:
        def helper(x: str | list) -> tuple:
            return tuple(map(x.index, x))

        s = s.split(' ')
        if len(pattern) != len(s): return False

        return helper(pattern) == helper(s)