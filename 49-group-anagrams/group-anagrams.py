from collections import defaultdict

class Solution:
    # O(n), O(n)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for word in strs:
            key = tuple(sorted(word))
            d[key].append(word)

        return list(d.values())