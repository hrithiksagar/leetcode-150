class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = -1
        # count = {}
        
        # for i in s:
        #     print(i)
        #     if i in count:
        #         count[i] += 1 
        #     else:
        #         count[i] = 1
        # print(count)
        
                
        # for i in range(len(s)):
        #     if count[s[i]] == 1:
        #         ans = i
        #         return ans
        
        
        count = defaultdict(int)
        for c in s:
            count[c]+=1
        
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
            
        return ans