class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(' ','') # remove spaces
        s = re.sub(r'[^a-z0-9]', '', s)
        print(s)
        if s == s[::-1]:
            return True 
        return False
        