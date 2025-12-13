from collections import defaultdict

class Solution:
    def countElements(self, arr: List[int]) -> int:
        seen = set()
        pending = defaultdict(int)
        ans = 0
        
        for x in arr:
            # CHECK 1: Is x valid right now?
            # If we have already seen x+1, then this x is valid immediately.
            if (x + 1) in seen:
                ans += 1
            else:
                # If not, mark this x as "waiting" for a future x+1
                pending[x] += 1
            
            # CHECK 2: Does x validate previous numbers?
            # If this is the first time we see x, it satisfies all pending (x-1)s.
            if x not in seen:
                if (x - 1) in pending:
                    ans += pending[x - 1]
                    pending[x - 1] = 0  # Clear them, they are counted now
                seen.add(x)
                
        return ans