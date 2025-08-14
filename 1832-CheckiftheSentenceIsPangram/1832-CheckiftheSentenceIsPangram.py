# Last updated: 8/14/2025, 1:21:47 AM
class Solution:
    # O(n), O(26)
    def checkIfPangram(self, sentence: str) -> bool:
        uni_s = set()

        for char in sentence:
            uni_s.add(char)

        return len(uni_s) == 26

