# Last updated: 8/8/2025, 11:01:26 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        def helper(l: List) -> List:
            i, j = 0, len(l) - 1
            while i < j:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
            
            return ''.join(l)
        
        res = s.split(' ')
        for i, l in enumerate(res):
            res[i] = helper(list(l))
        
        return ' '.join(res)
