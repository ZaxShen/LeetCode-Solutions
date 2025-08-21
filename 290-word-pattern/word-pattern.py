from collections import defaultdict

class Solution:
    # O(n), O(n)
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(pattern) != len(s):
            return False

        hash_p = defaultdict(list)
        hash_s = defaultdict(list)
        for i in range(len(pattern)):
            hash_p[pattern[i]].append(i)
            hash_s[s[i]].append(i)

        return tuple(hash_p.values()) == tuple(hash_s.values())