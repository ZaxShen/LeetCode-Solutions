from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        asc_q = deque()
        desc_q = deque()
        res = left = 0

        # 8
        # 8

        # 2
        # 8, 2

        # 2, 4
        # 8, 4

        # 2, 4, 7
        # 8, 7

        for idx, i in enumerate(nums):
            while asc_q and asc_q[-1] > i:
                asc_q.pop()
            asc_q.append(i)

            while desc_q and desc_q[-1] < i:
                desc_q.pop()
            desc_q.append(i)

            while desc_q[0] - asc_q[0] > limit:
                # Either operate desc_q or asc_q
                # [8, 2, 4]
                if nums[left] == desc_q[0]:
                    desc_q.popleft()
                elif nums[left] == asc_q[0]:
                    asc_q.popleft()
                left += 1
            res = max(res, idx - left + 1)

        return res