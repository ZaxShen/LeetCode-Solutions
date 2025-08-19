class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}
        x = y = 0

        for move in path:
            x += (move == 'E') - (move == 'W')
            y += (move == 'N') - (move == 'S')

            pos = (x, y)
            if pos in visited:
                return True
            visited.add(pos)

        return False
