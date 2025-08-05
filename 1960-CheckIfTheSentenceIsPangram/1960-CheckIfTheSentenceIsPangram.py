# Last updated: 8/4/2025, 10:44:00 PM
class Solution:
    # O(n), O(n)
    def checkIfPangram(self, sentence: str) -> bool:
        hashmap = {}

        for i in sentence:
            hashmap[i] = hashmap.get(i, 0) + 1

        return len(hashmap) == 26