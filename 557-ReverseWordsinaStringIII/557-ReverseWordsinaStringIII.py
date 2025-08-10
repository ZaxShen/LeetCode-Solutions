# Last updated: 8/10/2025, 2:49:55 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        def helper(word: str) -> str:
            word = list(word)
            left, right = 0, len(word) - 1
            while left < right:
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1
            
            return ''.join(word)
        
        return ' '.join(helper(word) for word in s.split())