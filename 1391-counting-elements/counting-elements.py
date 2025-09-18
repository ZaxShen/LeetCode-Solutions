class Solution:
    def countElements(self, arr: List[int]) -> int:
        hashset = set(arr)
        res = 0

        for num in arr:
            if num + 1 in hashset:
                res += 1

        return res