class Solution:
    # O(n), O(n)
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []

        for p in path:
            if p not in ('..', '', '.'):
                stack.append(p)
            elif stack and p == '..':
                stack.pop()

        return '/' + '/'.join(stack)