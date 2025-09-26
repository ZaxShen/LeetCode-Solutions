class Solution:
    def simplifyPath(self, path: str) -> str:
        path = list(filter(None, path.split('/')))
        stack = []

        for p in path:
            if stack and p == '..':
                stack.pop()
            elif p not in ('.', '..'):
                stack.append(p)

        return '/' + '/'.join(stack)