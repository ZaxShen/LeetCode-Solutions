from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        seen[0] = -1
        prefix = res = 0

        for idx, i in enumerate(nums):
            if i == 1:
                prefix += 1
            else:
                prefix -= 1

            if prefix in seen:
                res = max(res, idx - seen[prefix])
            # Store the first occurance for longest result
            else:
                seen[prefix] = idx

        print(seen)
        return res