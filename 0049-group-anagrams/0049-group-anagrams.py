# # # from collections import defaultdict #2 Calling default dict

# # # class Solution(object):
# # #     def groupAnagrams(self, strs):
# # #         """
# # #         :type strs: List[str]
# # #         :rtype: List[List[str]]
# # #         """
# # #         anagram_map = defaultdict(list)
# # #         result = []

# # #         for s in strs:
# # #             sorted_s = tuple(sorted(s))
# # #             anagram_map[sorted_s].append(s) #1. we didnt initialize key yet, so shuld call defaultdict
# # #             #3. mistake 2, we are using sorted s as ourt key however, when we run sorted method on string we get list obj back, lists are mutavble, mutable datatypes cant be keys so we need to convert this list into touple
# # #             for value in anagram_map.values():
# # #                 result.append(value)

# # #             return result


# # from collections import defaultdict

# # class Solution:
# #     def groupAnagrams(self, strs):
# #         letters_to_words = defaultdict(list)
# #         for word in strs:
# #             letters_to_words[tuple(sorted(word))].append(word)
# #         return list(letters_to_words.values())
        

# from collections import defaultdict
# class Solution:
#     def groupAnagrams(self, strs): 
#         res = defaultdict(list) #mapping character count of each word to list of anagramd
#         for s in strs:
#             count = [0]*26 # a.....z
#             for c in s:
#                 count[ord(c)-ord("a")] += 1
#             res[tuple(count)].append(s)
#         return res.values()
                



    
    
    
    
    
    
    
    
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs): 
#         https://youtu.be/9_iwjawJhdc
        # solution: first we will try to create a key value pair of elements, i.e. if a element eat and tea are same, make one of the element as key and other value, so here lets tale eat and key and sort it as 
        # aet: [eat, tea]
        # so now tea will be value of that key eat, even eat will be one value as we sorted those elements and made it a key and we need to return those in the end right. 
        # any key by default has em empyt list then weather or not that exists in the dictionary i need to add it in it
        dic = defaultdict(list) # default dictionary of a list 
        # iterate through every single word in the string, what this allows to do is instead of checking if my key is present and if so appending my word to existing list or if not already present then create new list at that key and add my word to it , any key by default has an empty list so weather or not this key exists all i have to do is append my word to this list. 
        for word in strs: # iterate through every single word in the list
            # print("".join(sorted(word)))
            dic["".join(sorted(word))].append(word) # this is going to be a key for thr dictionary
        return dic.values()
            
        
        



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        








        

         