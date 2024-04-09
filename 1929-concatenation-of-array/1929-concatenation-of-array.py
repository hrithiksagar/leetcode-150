class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans =[0] * (len(nums)*2)
        ans = nums + nums
        return ans

        
        
        
        
        
        
        
        
        
        
        # n = len(nums)
        # ans = [0] * (2*n)
        # print(len(ans))

        
        
        

        