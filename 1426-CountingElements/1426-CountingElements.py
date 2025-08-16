# Last updated: 8/16/2025, 12:33:20 PM
class Solution:
    # O(nlogn), O(1)
    def countElements(self, arr: List[int]) -> int:
        hashset = set(arr)
        res = 0

        for num in arr:
            if num + 1 in hashset:
                res += 1

        return res
