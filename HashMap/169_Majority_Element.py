'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = {}
        majority = 0
        ct = 0
        for num in nums:
            if num not in n:
                n[num] = []
            n[num].append(num)

        for k, v in n.items():
            if len(v) > ct:
                ct = len(v)
                majority = k
        return majority

sol = Solution()
nums = [2,2,1,1,1,2,2]
print(sol.majorityElement(nums))

