'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]
'''
from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        count = defaultdict(int)
        res = [0] * k

        for n in nums:
            count[n] += 1

        return sorted(count.items(), key=lambda x: x[1], reverse=True)[:k]

nums = [1,1,1,2,2,3]
k = 2
sol = Solution()
print(sol.topKFrequent(nums, k))
