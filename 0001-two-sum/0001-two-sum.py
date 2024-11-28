class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # number -> idx
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [i, seen[diff]]
            seen[nums[i]] = i
        return [-1,-1]