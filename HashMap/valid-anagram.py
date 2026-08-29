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
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s is None or t is None:
            return False

        letters = {}

        for l in s:
            if l not in letters.keys():
                letters[l] = 1
            else:
                letters[l] = letters.get(l) + 1
        
        for l in t:
            if l in letters[]
s = "racecar"
t = "carrace"
sol = Solution()
print(sol.isAnagram(s, t))
