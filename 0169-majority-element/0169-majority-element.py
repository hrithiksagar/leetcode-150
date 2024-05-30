class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        occ = {} # created a empty dict to store key and value (key = element in the list & value = number of times it occured)
        
        for i in nums:
            if i in occ:
                occ[i]+=1
            else:
                occ[i] = 1
        max_element = None
        max_count = 0

        for i, count in occ.items():
            if count > max_count:
                max_count = count  # Update the maximum count
                max_element = i  # Update the element with the maximum count
        return max_element
                
        