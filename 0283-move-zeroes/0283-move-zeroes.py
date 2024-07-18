class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0  # Initialize the left pointer
    
        for right in range(len(nums)):  # Iterate through the array with the right pointer
            if nums[right] != 0:  # When a non-zero element is found
                # Swap the elements at the left and right pointers
                nums[left], nums[right] = nums[right], nums[left]
                left += 1  # Increment the left pointer