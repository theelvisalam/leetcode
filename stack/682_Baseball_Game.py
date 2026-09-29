'''
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

Given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x: Record a new score of x.
'+': Record a new score that is the sum of the previous two scores.
'D': Record a new score that is the double of the previous score.
'C': Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

Note: The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.
'''
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            if op == '+':
                second = record.pop()
                first = record.pop()
                record.append(first)
                record.append(second)
                record.append(first + second)
            elif op == 'D':
                prev = record.pop()
                record.append(prev)
                record.append(prev * 2)
            elif op == 'C':
                record.pop()
            else:
                record.append(int(op))

        output = 0
        for r in record:
            output += r
        return output