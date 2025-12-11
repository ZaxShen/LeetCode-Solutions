class Solution:
    # O(n), O(1)
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        max_num = len(nums)

        exp_sum = (0 + max_num) * (n / 2)
        act_sum = sum(nums)

        return int(exp_sum - act_sum)