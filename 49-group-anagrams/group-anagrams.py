from collections import defaultdict, Counter

class Solution:
    # O(n), O(n)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for word in strs:
            count = Counter(word)
            key = tuple(sorted(count.items()))
            d[key].append(word)

        return list(d.values())