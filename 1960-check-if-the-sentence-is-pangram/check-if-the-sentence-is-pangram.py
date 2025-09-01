class Solution:
    # O(n), O(k)
    def checkIfPangram(self, sentence: str) -> bool:
        hashset = set()

        for char in sentence:
            hashset.add(char)
            # Early termination
            if len(hashset) == 26:
                return True

        return len(hashset) == 26