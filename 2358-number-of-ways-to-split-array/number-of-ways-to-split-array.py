class Solution:
    # O(n), O(1)
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sec = res = 0

        for i in nums[:-1]:
            left_sec += i
            right_sec = total - left_sec
            if left_sec >= right_sec: res += 1

        return res
