'''
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"

Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:

Input: s = "xyz", t = "xyz"

Output: "xyz"

Example 3:

Input: s = "x", t = "xy"

Output: ""

Constraints:

    1 <= s.length <= 100,000
    1 <= t.length <= 100,000
    s and t consist of uppercase and lowercase English letters.
'''
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        sub_strings = []
        l = r = 0

        while r < len(s):
            if s[r] in need:
                need[s[r]] -= 1
            r += 1
            if all(v == 0 for v in need.values()):
                window_string = "".join(x for x in s[l : r])
                sub_strings.append(window_string)
                l += 1
                while s[l] not in need:
                    l += 1
                need = Counter(t)
                r = l

        return min(sub_strings, key=len) if sub_strings else ""

s = "OUZODYXAZV"
t = "XYZ"
sol = Solution()
print(sol.minWindow(s,t))
