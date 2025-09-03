class Solution:
    def customSortString(self, order: str, s: str) -> str:
        return ''.join(sorted(s, key = lambda x: order.find(x) if x in s else len(order)))