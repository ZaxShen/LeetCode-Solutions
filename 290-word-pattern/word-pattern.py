class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        
        return tuple(map(pattern.index, pattern)) == tuple(map(s.index, s))