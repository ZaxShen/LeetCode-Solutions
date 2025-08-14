# Last updated: 8/14/2025, 1:25:23 AM
from collections import Counter

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        counter = Counter(sentence)

        return len(counter.keys()) == 26