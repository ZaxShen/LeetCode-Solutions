# Last updated: 8/4/2025, 10:46:28 PM
import collections

class Solution:
    # O(n), O(n)
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1
        q = collections.deque()

        while left <= right:
            _left, _right = nums[left]**2, nums[right]**2
            print(_left, _right)
            if _left <= _right:
                q.appendleft(_right)
                right -= 1
            else:
                q.appendleft(_left)
                left += 1
        
        return list(q)