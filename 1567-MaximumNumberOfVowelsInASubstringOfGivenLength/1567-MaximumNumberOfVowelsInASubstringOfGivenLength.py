# Last updated: 8/4/2025, 10:45:11 PM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        count_vowels = 0
        for char in s[:k]:
            count_vowels += int(char in vowels)
        
        left = 0
        max_vowels = count_vowels
        for i in range(k, len(s)):
            count_vowels += int(s[i] in vowels) - int(s[i-k] in vowels)
            max_vowels = max(max_vowels, count_vowels)
            # if max_vowels == k:
            #     return max_vowels

        return max_vowels
