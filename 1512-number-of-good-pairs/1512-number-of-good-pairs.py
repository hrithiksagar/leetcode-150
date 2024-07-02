class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        count = {} # n --> c
        for n in nums:
            if n in count:
                res +=count[n]
                count[n]+=1
            else:
                count[n] = 1
        return res
        
        