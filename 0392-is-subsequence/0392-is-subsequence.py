class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0

        while i<len(s) and j<len(t):
            print("before logic: ",i)
            if s[i] == t[j]:
                i+=1
                print("     in if loop, i= ", i)
                j+=1
                print("     in if loop, j= ", j)
            else:
                j+=1
                print("         in else loop, j= ", j)
        return i==len(s)

            











        # i =0
        # j = 0
        # while i<len(s) and j<len(t):
        #     if s[i] == t[j]:
        #         i+=1
        #         j+=1
        #     else:
        #         j+=1

        # return True if i==len(s) else False


        

        