class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        duplicate = -1
        missing = -1
        count = [0]*(n+1)
        
        for num in nums:
            count[num]+=1
        print(count)
        
        for i in range(1, n+1):
            if count[i]>1:
                duplicate = i
            elif count[i] == 0:
                missing = i
        return [duplicate, missing]
            
                