class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # maxproduct = (nums[n]*nums[n-1])-(nums[0]*nums[1])
        nums = sorted(nums)  # Sort the list once outside the loop
        n = len(nums)
        maxproduct = 0
        
        for i in range(n-1):  # Loop should run up to n-2
            print(nums[i], nums[i+1], nums[n-1])
            maxproduct = max(maxproduct, (nums[n-1]*nums[n-2])-(nums[i]*nums[i+1]))
            return maxproduct
            
        
        