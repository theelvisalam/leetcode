'''
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

    Each row must contain the digits 1-9 without duplicates.
    Each column must contain the digits 1-9 without duplicates.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = {}
        cols = {}
        subs = {}

        for row in range(9):
            d=
            for col in range(9):
                rows[row] = board[row]
                cols[col] = board[col]
        print(rows)
        pr:


board = [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"
    [".",".",".","8",".","3",".",".","jk5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
]
sol = Solution()
print(sol.isValidSudoku(board))
