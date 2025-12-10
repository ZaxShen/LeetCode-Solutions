class Solution:
	# O(n), O(k)
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        
        prefix = res = 0
        
        for i in nums:
            prefix += i
            remainder = prefix % k
            
            if remainder in count:
                res += count[remainder]
            count[remainder] += 1
        
        return res