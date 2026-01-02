class Solution:
    # O(n), O(k)
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        res = left = win_sum = 0

        for i in nums:
            win_sum += i
            while i in seen:
                win_sum -= nums[left]
                seen.remove(nums[left])
                left += 1
            seen.add(i)
            res = max(res, win_sum)

        return res