from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        aq = deque()
        dq = deque()
        res = left = 0

        for right, i in enumerate(nums):
            while aq and aq[-1] > i:
                aq.pop()
            aq.append(i)

            while dq and dq[-1] < i:
                dq.pop()
            dq.append(i)

            while dq[0] - aq[0] > limit:
                if dq[0] == nums[left]:
                    dq.popleft()
                elif aq[0] == nums[left]:
                    aq.popleft()
                left += 1
            
            res = max(res, right - left + 1)

        return res