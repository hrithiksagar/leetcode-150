class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        missing = []
        for i in nums:
            pos = abs(i)-1 # -1 because we want to use indices not positions
            if nums[pos]>0: # is not marked, so we mark it
                nums[pos]*= -1
        
        for i in range(len(nums)):
            if nums[i] >0: #i.e., its not been seen yet
                missing.append(i+1)
                
        return missing
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
"""
So what we are doing is:
we have to do this in place and not use a extra space, so for this we need to use a smart method.
that is, we need to mark all the visited elements so that we know that is not present in the list for ex:
if array nums = [1,2,3,4,1]
we take absolute values so index starts at 1 not 0
we mark index with [i*(-1)] at the position we are present 
1. so at index 1, the element is 1, so we mark index 1. (mark =[index*(-1)])
nums = [-1,2, 3, 4,1]
2. at index 2, element is 2, so we mark index 2.
nums = [-1,-2, -3, 4,1]
3. at index 2, element is 3, so we mark index 3.
nums = [-1,-2, -3, -4,1]
4. at index 3, element is 1, but 1 is already marked, so now we end the iteration. we see thweir positions and we return those positions+1
create new iteration for which we take the elements which are only unmarked
we append the missing list with those index and return it

"""
#         missing = []
#         for i in nums:
#             pos = abs(i)-1
#             if nums[pos]>0:
#                 nums[pos] *= -1

#         for i in range(len(nums)):
#             if nums[i]>0:
#                 missing.append(i+1)
#         return missing

            
        