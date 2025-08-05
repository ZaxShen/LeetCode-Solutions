# Last updated: 8/4/2025, 10:46:39 PM
from collections import defaultdict

class Solution:
    # O(n), O(k)
    def customSortString(self, order: str, s: str) -> str:
        common_set = set(order) & set(s)
        s_count = defaultdict(int)

        for char in s:
            if char in common_set:
                s_count[char] += 1

        res = ""
        for i in order:
            if i in s_count:
                res += i * s_count[i]

        for i in s:
            if i not in common_set:
                res += i

        return res