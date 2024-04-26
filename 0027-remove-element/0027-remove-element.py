class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[count] = nums[i]
                count += 1
        return count
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        # k = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         # partition of all values in nums not in nums and putting them in begenning
        #         nums[k] = nums[i]
        #         k += 1
        # return k
        

        