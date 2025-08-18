class Solution:
    # O(n), O(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = curr = 0
        res = float('inf')

        for right, num in enumerate(nums):
            curr += num

            while curr >= target:
                res = min(res, right - left + 1)
                curr -= nums[left]
                left += 1


        return res if res != float('inf') else 0
