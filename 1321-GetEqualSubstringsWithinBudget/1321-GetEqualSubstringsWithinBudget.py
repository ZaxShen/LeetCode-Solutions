# Last updated: 8/4/2025, 10:45:48 PM
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = [abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)]
        
        curr_cost = max_len = left = 0
        for right, v in enumerate(costs):
            curr_cost += v
            while curr_cost > maxCost:
                curr_cost -= costs[left]
                left += 1
            max_len = max(max_len, right - left + 1)
            
        return max_len