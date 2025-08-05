# Last updated: 8/5/2025, 12:18:59 AM
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        hashset = {(x, y)}

        for p in path:
            if p == 'N':
                y += 1
            elif p == 'S':
                y -= 1
            elif p == 'E':
                x += 1
            elif p == 'W':
                x -= 1
            if (x, y) in hashset:
                return True
            hashset.add((x, y))

        return False