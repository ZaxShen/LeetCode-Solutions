class Solution:
    def simplifyPath(self, path: str) -> str:
        path = list(filter(None, path.split('/')))
        stack = []

        for p in path:
            if p == '.':
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)

        return '/' + '/'.join(stack)