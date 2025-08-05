# Last updated: 8/4/2025, 10:45:38 PM
class Solution:
    # O(n), O(n)
    def countElements(self, arr: list[int]) -> int:
        hash_set = set(arr)
        count = 0
        
        for i in arr:
            if i + 1 in hash_set:
                count += 1
            
        return count