class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        visited = {(x, y)} # Init visited with the original point

        for i in path:
            match i:
                case 'N': y += 1
                case 'S': y -= 1
                case 'E': x += 1
                case 'W': x -= 1

            loc = (x, y)
            if loc in visited:
                return True
            visited.add(loc)

        return False
