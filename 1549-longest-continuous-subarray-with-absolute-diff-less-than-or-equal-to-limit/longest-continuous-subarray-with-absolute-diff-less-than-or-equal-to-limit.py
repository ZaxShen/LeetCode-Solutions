from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        aq = deque()
        dq = deque()
        res = left = 0

        for right, num in enumerate(nums):
            while aq and aq[-1] > num:
                aq.pop()
            aq.append(num)

            while dq and dq[-1] < num:
                dq.pop()
            dq.append(num)

            # 4
            # 2

            # 8, 4
            # 2, 4
            while dq[0] - aq[0] > limit:
                if dq[0] == nums[left]:
                    dq.popleft()
                if aq[0] == nums[left]:
                    aq.popleft()
                left += 1

            res = max(res, right - left + 1)

        return res

            
