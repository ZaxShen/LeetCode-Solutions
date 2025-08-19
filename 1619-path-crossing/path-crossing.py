class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        visited = {(0, 0)}
        
        for direction in path:
            # Avoid multiple if-elif by using match (Python 3.10+)
            match direction:
                case 'N': y += 1
                case 'S': y -= 1
                case 'E': x += 1
                case 'W': x -= 1
            
            pos = (x, y)
            if pos in visited:
                return True
            visited.add(pos)
        
        return False