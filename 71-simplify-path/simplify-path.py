class Solution:
    # O(n), O(n)
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []

        for p in path:
            if p == '.':
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            elif p != '':
                stack.append(p)

        return '/' + '/'.join(stack)
        