'''
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true

Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:

Input: s1 = "abc", s2 = "lecaabee"

Output: false

Constraints:

    1 <= s1.length, s2.length <= 10000
'''
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        l = 0

        for r in range(len(s2)):
            if s2[r] in need.keys():
                need[s2[r]] -= 1
            while (r - l + 1) > len(s1):
                if s2[l] in need:
                    need[s2[l]] += 1
                l += 1
            if all(v == 0 for v in need.values()):
                return True
        return False
                


        
s1 = "abc"
s2 = "lecabee"
sol = Solution()
print(sol.checkInclusion(s1, s2))
