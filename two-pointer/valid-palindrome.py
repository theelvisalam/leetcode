'''
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true

Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false

Explanation: "tabacat" is not a palindrome.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # chars = "".join(char.lower() for char in s if char.isalnum())
        l, r = 0,len(s) - 1

        while l < r:
            lchar = s[l]
            rchar = s[r]
            if lchar.isalnum() and rchar.isalnum():
                if lchar.lower() == rchar.lower():
                    l += 1
                    r -= 1
                else:
                    return False
            if not lchar.isalnum():
                l += 1
            if not rchar.isalnum():
                r -= 1

        return True

        
s = "Was it a car or a cat I saw?"
sol = Solution()
print(sol.isPalindrome(s))
