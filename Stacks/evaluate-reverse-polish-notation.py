'''
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

    The operands may be integers or the results of other operations.
    The operators include '+', '-', '*', and '/'.
    Assume that division between integers always truncates toward zero.

Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens) - 1, -1, -1):
            stack.append(tokens[i])

        while stack:
            if stack[-1] is in "+-*/":
                op = stack.pop()
                if op == "-":
                    
                if op == "+":
                if op == "*":
                if op == "/":
            else:
                a = stack.pop()
                b = stack.pop()

                
tokens = ["1","2","+","3","*","4","-"]
sol = Solution()
print(sol.evalRPN(tokens))
