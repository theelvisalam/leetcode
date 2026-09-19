'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

Two strings are anagrams if they contain the same characters, with each character appearing the same number of times, regardless of order.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true


Example 2:

Input: s = "jar", t = "jam"

Output: false


Example 3:

Input: s = "x", t = "x"

Output: true
'''
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        lt = defaultdict(int)
        ls = defaultdict(int)
        
        for l in t:
            lt[l] += 1

        for l in s:
            ls[l] += 1

        for l, i in lt.items():
            if ls[l] != i:
               return False
        return True

s = "racecar"
t = "carrace"
sol = Solution()
print(sol.isAnagram(s, t))
