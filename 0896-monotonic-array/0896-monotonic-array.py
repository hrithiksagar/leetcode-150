class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if a monotonus decrease is reversed then it becomes monotonus increase. then we will have only one loop to work with else we would need 2. 
        if nums[-1]-nums[0]<0: # last element - first element < 0 then it is monotnus decrease we will reverse this
            nums.reverse()
            
        # now array is monotnous increase
        for i in range(len(nums)-1): #-1 because i+1 exists in the loop
            if not (nums[i]<=nums[i+1]):
                return False
        return True
        
        