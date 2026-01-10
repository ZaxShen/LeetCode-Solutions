class Solution:
    # O(n+m), O(n+m)
    def isIsomorphic(self, s: str, t: str) -> bool:
        return tuple(map(s.index, s)) == tuple(map(t.index, t))