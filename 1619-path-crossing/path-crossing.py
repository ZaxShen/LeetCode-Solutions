class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = {(x, y)}

        for move in path:
            match move:
                case 'N': y += 1
                case 'S': y -= 1
                case 'E': x += 1
                case 'W': x -= 1

            pos = (x, y)
            if pos in visited:
                return True
            visited.add(pos)

        return False