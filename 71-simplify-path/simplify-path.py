class Solution:
    # O(n), O(n)
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []

        for p in path:
            if p == '..':
                if stack:
                    stack.pop()
            elif p not in ('', '.'):
                stack.append(p)

        return '/' + '/'.join(stack)
        