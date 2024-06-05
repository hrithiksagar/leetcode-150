class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        numsOneIndex = {n:i for i,n in enumerate(nums1)}
        ans = [-1]*len(nums1)
        # print(numsOneIndex)
        
        for i in range(len(nums2)):
            if nums2[i] not in numsOneIndex:
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    index = numsOneIndex[nums2[i]]
                    ans[index] = nums2[j]
                    break
        return ans
                    
            
        
        
        
#         ans = [] * len(nums1) # base case
#         for i in range(len(nums1)):
#             for j in range(len(nums2)):
#                 if nums1[i] == nums2[j]:
#                     if nums2[j+1] > nums2[j]:
#                         ans.append(nums2[j+1])
#                     else:
#                         ans.append(-1)
#                 j+=1
                
#             i += 1 
#         return ans
        
    
        