class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')

        for i in path:
            # ''
            # .,
            # ..
            if i not in ('', '.', '..'):
                stack.append(i)
            elif stack and i == '..':
                stack.pop()

        return '/' + '/'.join(stack)