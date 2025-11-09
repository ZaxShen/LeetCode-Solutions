from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        aq = deque()
        dq = deque()
        left = res = 0

        for right, i in enumerate(nums):
            while aq and aq[-1] > i:
                aq.pop()
            aq.append(i)

            while dq and dq[-1] < i:
                dq.pop()
            dq.append(i)

            while dq and aq and dq[0] - aq[0] > limit:
                if nums[left] == dq[0]:
                    dq.popleft()
                elif nums[left] == aq[0]:
                    aq.popleft()
                left += 1
            else:
                res = max(res, right - left + 1)

        return res