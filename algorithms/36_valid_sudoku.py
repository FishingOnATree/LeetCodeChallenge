# https://leetcode.com/problems/valid-sudoku/#/description


class Solution(object):
    def isValidSudoku(self, board):
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]

        for row, row_content in enumerate(board):
            for col, cell in enumerate(row_content):
                if cell != ".":
                    box_num = (row // 3) * 3 + (col // 3)
                    if cell in row_set[row] or cell in col_set[col] or cell in box_set[box_num]:
                        return False
                    else:
                        row_set[row].add(cell)
                        col_set[col].add(cell)
                        box_set[box_num].add(cell)
        return True

a = Solution()
print(a.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]))