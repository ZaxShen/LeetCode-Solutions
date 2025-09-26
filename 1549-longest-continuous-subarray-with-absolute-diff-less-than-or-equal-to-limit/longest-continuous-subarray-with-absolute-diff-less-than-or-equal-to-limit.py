from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        asc = deque()
        desc = deque()

        res = 0
        left = 0
        for right, num in enumerate(nums):
            while asc and asc[-1] > num:
                asc.pop()
            asc.append(num)

            while desc and desc[-1] < num:
                desc.pop()
            desc.append(num)

            while desc[0] - asc[0] > limit:
                if nums[left] == asc[0]:
                    asc.popleft()
                if nums[left] == desc[0]:
                    desc.popleft()
                left += 1

            res = max(res, right - left + 1)

        return res