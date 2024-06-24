class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        leftSum = 0 # initisally its 0 as we didnt visit any value
        for i in range(len(nums)):
            rightSum = total - nums[i]-leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1
                
        