class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(k) - at most k different remainders
        """
        # Hash map to store frequency of each remainder
        remainder_count = defaultdict(int)
        # Initialize with remainder 0 (empty prefix sum)
        remainder_count[0] = 1
        
        prefix_sum = 0
        result = 0
        
        for num in nums:
            # Update prefix sum
            prefix_sum += num
            
            # Calculate remainder (handle negative remainders)
            remainder = prefix_sum % k
            
            # In Python, negative % gives negative result
            # We need positive remainder: -1 % 5 should be 4
            # Python handles this correctly, but for clarity:
            # remainder = (remainder + k) % k  # not needed in Python
            
            # Add count of this remainder seen before
            # Each previous occurrence forms a valid subarray
            result += remainder_count[remainder]
            
            # Increment count for this remainder
            remainder_count[remainder] += 1
        
        return result