class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = [] # initializing prefix array
        cur = 0 # initially its empty
        for n in nums:
            cur += n
            self.prefix.append(cur)
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        rightSum = self.prefix[right]
        leftSum = self.prefix[left-1] if left>0 else 0
        return rightSum - leftSum

"""
to do it in O(1) if we have precouted sum, i.e., solving uing subarrays 
total sub arrays = O(n^2)
to do even better, we dont have to calculate sum of every single subarray, we can using prefix sum
prefix = any subarray that starts at the begenning of the array, can compute this in O(n) time. 
prefix = (0,1), (0,1,2), (0,1,2,3), (0,1,2,3,4....)
for example:
Example 1:
Array =  1,2,3,4,5
Prefix = 1,3,6,10,15 : sum of previous elemt+current element.

Example 2:
Array =  -2, 0,  3, -5,  2, -1
Prefix = -2, -2, 1, -4, -2, -3 : this is the sum previous 
how to use this prefix sum for our problem?
- without having to iterate through every single position?
- to find sum of left+....+right:
- Rightmost prefix - Left(Leftmost prefix) 

"""

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)