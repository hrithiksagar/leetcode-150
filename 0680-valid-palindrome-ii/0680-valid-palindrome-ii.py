class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def is_palindrome_range(s, left, right): # helper function, a regular Palindrome code. 
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
    
        left = 0
        right = len(s)-1
        
        while left < right:
            if s[left] != s[right]:
            # If there's a mismatch, check two possibilities:
            # 1. Skipping the left character
            # 2. Skipping the right character
                return is_palindrome_range(s, left + 1, right) or is_palindrome_range(s, left, right - 1)
            left += 1
            right -= 1
    
        return True
        
        