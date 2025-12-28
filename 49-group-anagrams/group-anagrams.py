from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in strs:
            hashmap[tuple(sorted(i))].append(i)

        return list(hashmap.values())