'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

String encode(List<String> strs) {
    // ... your code
    return encoded_string;
}

Machine 2 (receiver) has the function:

List<String> decode(String encoded_string) {
    // ... your code
    return decoded_strs;
}

So Machine 1 does:

String encoded_string = encode(strs);

and Machine 2 does:

List<String> decoded_strs = decode(encoded_string);

decoded_strs in Machine 2 should be the same as the input strs in Machine 1.

Implement the encode and decode methods.

Example 1:

Input: strs = ["Hello","World"]

Output: ["Hello","World"]

Explanation:

Solution solution = new Solution();
String encoded_string = solution.encode(strs);

// Machine 1 ---encoded_string---> Machine 2

List<String> decoded_strs = solution.decode(encoded_string);


Example 2:

Input: strs = [""]

Output: [""]
'''
class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs is None:
            return strs
        separator = "#"
        for word in strs:
            length = len(word)



    def decode(self, s: str) -> List[str]:

strs = ["Hello","World"]
sol = Solution()
print(sol.encode(strs))
print(sol.decode(sol.encode(strs)))
