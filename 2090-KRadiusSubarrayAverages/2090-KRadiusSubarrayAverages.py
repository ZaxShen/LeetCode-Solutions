# Last updated: 8/10/2025, 11:37:03 PM
class Solution:
    # O(n), O(n)
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        curr, prefix_sum = 0, []

        for i in nums:
            curr += i
            prefix_sum.append(curr)

        res = []
        n = 2 * k + 1

        for i in range(len(prefix_sum)):
            left = i - k
            right = i + k
            if 0 <= left and right < len(nums):
                ans = (prefix_sum[right] - prefix_sum[left] + nums[left]) // n
                res.append(ans)
            else:
                res.append(-1)

        return res
