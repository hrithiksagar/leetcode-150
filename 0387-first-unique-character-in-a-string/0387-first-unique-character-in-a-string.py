class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = -1
        # charCount = Counter(s)
        # print(charCount)
        # print(len(s))
        count = {}
        for i in s:
            print(i)
            if i in count:
                count[i] += 1 
            else:
                count[i] = 1
        print(count)
        
        # for i in count:
        #     print(count[i])
        #     if count[i] == 1:
        #         print("i: ",i)
                
        for i in range(len(s)):
            if count[s[i]] == 1:
                ans = i
                return ans
            

        return ans