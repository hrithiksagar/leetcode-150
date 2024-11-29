class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # # Brute Force Approach
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        # return False

        # # Efficient Approach
            # Hashset
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False