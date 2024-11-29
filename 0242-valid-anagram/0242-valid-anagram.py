class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        # else: 
        #     set1 = set()
        #     set2 = set()
        #     for ele in s:
        #         set1.add(ele)
            
        #     for ele in t:
        #         set2.add(ele)
        #     print(set1)
        #     print("\n")
        #     print(set2)
        #     if set1 == set2:
        #         return True
        #     else:
        #         return False

