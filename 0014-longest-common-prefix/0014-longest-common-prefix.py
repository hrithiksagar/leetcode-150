class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        first find the smallest element in the list and assign it as a prefix,

        """

        ans = ""
        prefix = ""
        for i in strs:
            if (len(i)<len(prefix) or prefix ==""):
                prefix = i
        # here prefix = flow as its the smallest element
        # check that prefix (flow) with the other elements, if not then remove one word from prefix (flo) if even this is not matching with the element thsn. remove one more word from last of prefix (fl), now this element matches with 
        count = 0
        need = len(strs) # need is that we need answers from these all elements in the array if only some elements matches the prefix letters it wont count as answer, all the elements must be visited
        while (need != count):
            count = 0

            for i in strs:
                if prefix == i[:len(prefix)]: # here len(prefix) = 4 as flow is 4 letters
                    count += 1

            res = prefix
            prefix = prefix[:-1]
        
        if need == count:
            return res
        else:
            return ""


        















    
        # res = ""
        # for i in range(len(strs[0])): # going therough every single character i 1st string, because there is a chance that this is not the shortest string in whole string. 
        #     for s in strs:
        #         if i == len(s) or s[i] != strs[0][i]:
        #             return res

        #     res += strs[0][i]
        # return res



        