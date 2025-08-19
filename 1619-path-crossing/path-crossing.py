class Solution:
    # O(n), O(n)
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        visited = {(0, 0)}
        
        for d in path:
            x += (d == 'E') - (d == 'W')
            y += (d == 'N') - (d == 'S')
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False