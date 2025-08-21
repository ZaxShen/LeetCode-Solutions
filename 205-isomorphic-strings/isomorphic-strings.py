from collections import defaultdict

class Solution:
    # O(n), O(n)
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_s = defaultdict(list)
        hash_t = defaultdict(list)

        for i in range(len(s)):
            hash_s[s[i]].append(i)
            hash_t[t[i]].append(i)

        return tuple(hash_s.values()) == tuple(hash_t.values())