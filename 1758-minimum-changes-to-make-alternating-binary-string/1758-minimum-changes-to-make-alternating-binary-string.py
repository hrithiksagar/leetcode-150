class Solution:
    def minOperations(self, s: str) -> int:
        # final string looks like
        # case 1: 010101010...
        # case 2: 1010101010....
        # check for case 1 and Check for case 2. maybe 2 loops but can try to keep one. ans = min of both cases. 
        # s = [i for i in s]
        # s = 0 1 0 0 
        # s = 0 1 0 1 # ops = 1
        # s = 1 0 1 0 # ops = 3 min(3,1) = 1, ans = 1 
        # case 1
        
        count = 0
        
        # for i in range(len(s)):
        #     # even indices, even value, odd index odd value
        #     if i%2: # odd
        #         count += 1 if s[i] == "0" else 0
        #     else: # even
        #         count += 1 if s[i] == "1" else 0
        for i in range(len(s)):
            # even indices, even value, odd index odd value
            if i%2: # odd
                if s[i] == "0":
                    count+=1
                else:
                    count+=0
            else: # even
                if s[i] == "1":
                    count+=1
                else:
                    count+=0
        return min(count, len(s)-count)

        
        
        
        
        