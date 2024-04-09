class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        max_right = -1
        for i in range(n-1, -1, -1): # From last element, one step down, reverse
            tmp = arr[i]
            arr[i] = max_right
            max_right = max(max_right, tmp)
        return arr









        # # curr_max = arr[-1]
        # # arr[-1] = -1
        # # for i in range(len(arr)-2,-1,-1):
        # #     curr = arr[i]
        # #     arr[i] = curr_max
        # #     if curr>curr_max:
        # #         curr_max = curr
        # # return arr

        # # initial max = -1
        # # reverse iteraiton
        # # new max = max(oldmax, arr[i])
        # rightMax = -1
        # for i in range(len(arr)-1, -1, -1): # starts in reverse order and stops after reaching first element  
        #     newMax = max(rightMax, arr[i])
        #     arr[i] = rightMax # last value is equal to -1
        #     rightMax = newMax

        # return arr
        # range(n - 1, -1, -1): 
        # This creates a range that starts from n - 1 and goes down to 0 (inclusive), with a step of -1. In other words, it generates the sequence of integers [n - 1, n - 2, ..., 1, 0]. This is used to iterate over the indices of the array arr from right to left.

 
