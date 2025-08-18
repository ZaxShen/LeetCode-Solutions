class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def backtrack(nums):
            # Base case: if only one number left, check if it's close to 24
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            
            # Try all pairs of numbers
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        # Create new list without nums[i] and nums[j]
                        remaining = []
                        for k in range(len(nums)):
                            if k != i and k != j:
                                remaining.append(nums[k])
                        
                        # Try all 4 operations between nums[i] and nums[j]
                        a, b = nums[i], nums[j]
                        
                        # Addition: a + b = b + a (commutative)
                        if backtrack(remaining + [a + b]):
                            return True
                        
                        # Subtraction: a - b (not commutative)
                        if backtrack(remaining + [a - b]):
                            return True
                        
                        # Multiplication: a * b = b * a (commutative) 
                        if backtrack(remaining + [a * b]):
                            return True
                        
                        # Division: a / b (not commutative, avoid division by zero)
                        if abs(b) > 1e-6 and backtrack(remaining + [a / b]):
                            return True
            
            return False
        
        return backtrack([float(x) for x in cards])