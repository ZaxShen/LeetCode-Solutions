class Solution:
    def simplifyPath(self, path: str) -> str:
        path = list(filter(None, path.split('/')))
        stack = []

        for p in path:
            if p == '.':
                pass
            elif p == '..':
                if len(stack) >= 1:
                    stack.pop()
            else:
                stack.append(p)

        return '/' + '/'.join(stack)