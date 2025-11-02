class Solution:
    # O(n), O(1)
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        
        for i in path:
            # .
            # ..
            # ''
            if i not in ('', '..', '.'):
                stack.append(i)
            elif stack and i == '..':
                stack.pop()
            
        return '/' + '/'.join(stack)