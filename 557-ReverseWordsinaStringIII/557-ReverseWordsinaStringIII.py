# Last updated: 8/8/2025, 11:13:11 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        def helper(word: str) -> str:
            word = list(word)
            i, j = 0, len(word) - 1
            while i < j:
                word[i], word[j] = word[j], word[i]
                i += 1
                j -= 1
            
            return ''.join(word)
        
        return ' '.join(helper(word) for word in s.split())
