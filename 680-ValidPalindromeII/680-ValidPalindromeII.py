# Last updated: 8/8/2025, 12:53:11 AM
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        n = 1
        while i < j:
            if s[i] != s[j]:
                if n == 0:
                    return False
                else:
                    n -= 1
                    # Try both possibilities with inline palindrome checks
                    
                    # Option 1: Skip left character (check if s[i+1:j+1] is palindrome)
                    left, right = i + 1, j
                    is_option1_valid = True
                    while left < right:
                        if s[left] != s[right]:
                            is_option1_valid = False
                            break
                        left += 1
                        right -= 1
                    
                    # Option 2: Skip right character (check if s[i:j] is palindrome)
                    left, right = i, j - 1
                    is_option2_valid = True
                    while left < right:
                        if s[left] != s[right]:
                            is_option2_valid = False
                            break
                        left += 1
                        right -= 1
                    
                    return is_option1_valid or is_option2_valid
            else:
                i += 1
                j -= 1
        return True