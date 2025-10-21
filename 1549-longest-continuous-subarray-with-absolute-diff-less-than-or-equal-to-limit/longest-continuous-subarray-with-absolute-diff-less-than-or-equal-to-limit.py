from collections import deque

class Solution:
    # O(n), O(n)
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        aq = deque()
        dq = deque()

        res = left = 0
        for right, i in enumerate(nums):
            # Maintain deque in ascending order
            while aq and aq[-1] > i:
                aq.pop()
            aq.append(i)

            # Maintain deque in descending order
            while dq and dq[-1] < i:
                dq.pop()
            dq.append(i)

            # Shrink window while condition violated
            while dq[0] - aq[0] > limit:
                if nums[left] == dq[0]:
                    dq.popleft()
                if nums[left] == aq[0]:
                    aq.popleft()
                left += 1

            # Update maximum length
            res = max(res, right - left + 1)

        return res