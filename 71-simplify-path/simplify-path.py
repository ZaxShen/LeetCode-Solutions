class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')

        for p in path:
            if p not in ('..', '', '.'):
                stack.append(p)
            if stack:
                if p == '..':
                    stack.pop()

        return '/' + '/'.join(stack)