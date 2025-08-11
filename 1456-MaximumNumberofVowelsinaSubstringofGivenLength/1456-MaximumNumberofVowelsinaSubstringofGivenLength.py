# Last updated: 8/11/2025, 6:56:54 PM
class Solution:
    # O(n), O(1)
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        
        # Count vowels for in 1st window
        count = sum(char in vowels for char in s[:k])
        max_count = count

        # Sliding Window
        left = 0
        for right in range(k, len(s)):
            left = right - k
            count += (s[right] in vowels) - (s[left] in vowels)
            max_count = max(max_count, count)

        return max_count

