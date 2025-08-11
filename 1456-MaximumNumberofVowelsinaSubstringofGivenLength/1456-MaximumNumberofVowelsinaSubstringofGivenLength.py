# Last updated: 8/11/2025, 6:40:55 PM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ('a', 'e', 'i', 'o', 'u')
        max_vowels = count = left = 0
        
        for right, char in enumerate(s):
            if char in vowels:
                count += 1
                max_vowels = max(max_vowels, count)
            if right - left + 1 == k:
                if s[left] in vowels:
                    count -= 1
                left += 1
        
        return max_vowels

