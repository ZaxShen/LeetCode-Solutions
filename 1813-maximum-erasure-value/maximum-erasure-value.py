class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left = win_sum = res = 0

        for i in nums:
            win_sum += i
            while i in seen:
                win_sum -= nums[left]
                seen.remove(nums[left])
                left += 1
            seen.add(i)
            res = max(win_sum, res)

        return res