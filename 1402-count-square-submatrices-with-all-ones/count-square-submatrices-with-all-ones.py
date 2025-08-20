class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        total_count = 0
        
        # dp[i][j] = size of largest square with bottom-right at (i,j)
        dp = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        # First row or first column
                        dp[i][j] = 1
                    else:
                        # Square size = 1 + min of three neighbors
                        dp[i][j] = 1 + min(
                            dp[i-1][j],     # top
                            dp[i][j-1],     # left  
                            dp[i-1][j-1]    # top-left diagonal
                        )
                    
                    # dp[i][j] represents number of squares ending at (i,j)
                    total_count += dp[i][j]
        
        return total_count