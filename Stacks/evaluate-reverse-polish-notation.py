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
        stk = []

        for t in tokens:
            if t == "+":
                stk.append(stk.pop() + stk.pop())
            elif t == "-":
                a, b = stk.pop(), stk.pop()
                stk.append(b - a)
            elif t == "*":
                stk.append(stk.pop() * stk.pop())
            elif t == "/":
                a, b = stk.pop(), stk.pop()
                stk.append(int(float(b) / a))
            else:
                stk.append(int(t))

        return stk[0]

tokens = ["1","2","+","3","*","4","-"]
sol = Solution()
print(sol.evalRPN(tokens))
