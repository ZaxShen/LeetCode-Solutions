from collections import Counter

class Solution:
    # O(klogk), O(k)
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Edge Case
        if len(word1) != len(word2): return False

        c1, c2 = Counter(word1), Counter(word2)
        if c1.keys() != c2.keys(): return False

        return sorted(c1.values()) == sorted(c2.values())