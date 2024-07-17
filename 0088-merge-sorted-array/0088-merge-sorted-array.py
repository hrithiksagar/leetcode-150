class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1 = m+n-1 # end of nums1 original
        p2 = n-1 # end of nums2
        p3 = m-1 # end of nums1 till where elements are present
        
        # lets start adding nums2 elements into nums1 from end
        while p1>=0 and p2>=0:
            print("p1: ", p1)
            print("p2: ", p2)
            nums1[p1] = nums2[p2]
            p1-=1
            p2-=1
            print(nums1)
            
        nums1.sort()
        print(nums1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Solution 2
#         #get last index of num1
#         last = m+n-1
#         #start merging in reverse order
#         while m>0 and n>0:
#             if nums1[m-1]>nums2[n-1]:
#                 nums1[last]=nums1[m-1]
#                 m-=1
#             else:
#                 nums1[last]= nums2[n-1]
#                 n-= 1
#             last -= 1
        
#         #fill nums 1 with the leftover elementsb in nums2
#         while n>0:
#             nums1[last] = nums2[n-1]
#             n, last = n-1, last-1