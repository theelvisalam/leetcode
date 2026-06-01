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
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ct = {}
        fq = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            ct[n] = 1 + ct.get(n, 0)
        
        for n, c in ct.items():
            fq[c].append(n)

        for i in range(len(fq) - 1, 0, -1):
            for n in fq[i]:
                if len(res) < k:
                    res.append(n)
                else:
                    continue
                    
        return res