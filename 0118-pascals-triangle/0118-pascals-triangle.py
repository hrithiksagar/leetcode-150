class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]] #simple base case

        for i in range(numRows-1): #because we already made one row
            temp = [0]+ res[-1] + [0] #just building a new temporary list instead of modifying original list
            row = []
            for j in range(len(res[-1])+1): #length of this row is, previous row + 1 
                row.append(temp[j]+temp[j+1])
            res.append(row)

        return res

        