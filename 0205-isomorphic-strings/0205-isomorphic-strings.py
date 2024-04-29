class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Case 1 - if strings are not of eq
        # check keys and values both. 
        mapStoT = {} # hashmap
        mapTtoS = {} #hashmap2

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if ((c1 in mapStoT and mapStoT[c1] != c2) or (c2 in mapTtoS and mapTtoS[c2] != c1)):
                return False
        
            mapStoT[c1] = c2
            mapTtoS[c2] = c1
        return True
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         mapStoT = {} # hashmap
#         mapTtoS = {} #hashmap2

#         for i in range(len(s)):
#             c1 = s[i]
#             c2 = t[i]
#             if ((c1 in mapStoT and mapStoT[c1] != c2) or 
#             (c2 in mapTtoS and mapTtoS[c2] != c1)):
#                 return False
        
#             mapStoT[c1] = c2
#             mapTtoS[c2] = c1
#         return True
         