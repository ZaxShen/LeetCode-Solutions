class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return tuple(map(s.index, s)) == tuple(map(t.index, t))