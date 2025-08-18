class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = curr = 0
        res = float('inf')

        for right, num in enumerate(nums):
            curr += num

            while left <= right and curr >= target:
                res = min(res, right - left + 1)
                curr -= nums[left]
                left += 1


        return res if res != float('inf') else 0
