class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        # step 1: Extract all 3 length sub string 
            # to do this, we need to iterate over len(num)-2 inorder to form 3 length strings
        for i in range(len(num)-2):
            substrings = num[i:i+3]
            print(substrings)
            
            if substrings[0]==substrings[1]==substrings[2]:
                if substrings>res:
                    res = substrings
            
        return res