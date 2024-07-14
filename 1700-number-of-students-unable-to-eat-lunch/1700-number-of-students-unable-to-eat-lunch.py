class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
#         res = len(students)
        
#         # count occurances of students and their preferences
#         count = {} # hashmap
#         for s in students:
#             if s not in count:
#                 count[s] = 0
#             count[s] += 1
        
#         # count = Counter(students) # do same thing as above
        
#         for s in sandwiches:
#             if count[s] > 0:
#                 res -= 1
#                 count[s] -= 1
#             else:
#                 return res
#         return res
        count_0 = students.count(0) 
        count_1 = students.count(1)

        # Go through each sandwich in the stack
        for sandwich in sandwiches:
            if sandwich == 0 and count_0 > 0:
                count_0 -= 1
            elif sandwich == 1 and count_1 > 0:
                count_1 -= 1
            else:
                break  # No student wants this sandwich, break the loop

        # The number of students unable to eat is the sum of remaining counts
        return count_0 + count_1