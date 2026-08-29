'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true


Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ct = {}

        for num in nums:
            if num not in ct.keys():
                ct[num] = 1
            else:
                ct[num] = ct.get(num) + 1
        
        for numCt in ct.values():
            if numCt >= 2:
                return True

        return False

        
input = [1, 2, 3, 3]
sol = Solution()
print(sol.hasDuplicate(input))
