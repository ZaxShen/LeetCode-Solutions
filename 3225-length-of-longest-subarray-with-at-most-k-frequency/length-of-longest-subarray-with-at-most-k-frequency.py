class Solution:
    # O(n), O(k)
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = {}
        left = res = 0
        for right, num in enumerate(nums):
            count[num] = count.get(num, 0) + 1
            
            while count[num] > k:
                count[nums[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)

        return res