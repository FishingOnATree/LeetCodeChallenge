# https://leetcode.com/problems/sudoku-solver/


class Solution(object):
    def solveSudoku(self, board):
        num_board = []
        for row in board:
            num_board.append([0 if letter == "." else int(letter) for letter in row])
        blank_cell_size = -1
        while True:
            possible_dict = {}
            for i in range(9):
                for j in range(9):
                    if num_board[i][j] == 0:
                        possibility = self.list_possibility(num_board, i, j)
                        if len(possibility) == 1:
                            num_board[i][j] = possibility.pop()
                        else:
                            possible_dict[tuple((i, j))] = possibility
            if len(possible_dict) == 0:
                break
            elif blank_cell_size == len(possible_dict):
                count = len(possible_dict)
                for key, value in possible_dict.items():
                    row, col = key
                    possibility = self.list_permutation_possibility(possible_dict, row, col)
                    if len(possibility) == 1:
                        num_board[row][col] = possibility.pop()
                        count -= 1
                if count == blank_cell_size:
                    # do something here
                    break
                else:
                    blank_cell_size = count
            else:
                blank_cell_size = len(possible_dict)
        for i in range(9):
            board[i] = "".join([str(num_board[i][j]) for j in range(9)])

    @staticmethod
    def list_permutation_possibility(possible_dict, row, col):
        permutation = set(possible_dict[tuple((row, col))])
        for key, value in possible_dict.items():
            i, j = key
            row_base = row // 3
            col_base = col // 3
            # really XOR here so that either i==row or j==col but not the same time.
            if i == row or j == col or (row_base*3 <= i <= row_base*3+2 and col_base*3 <= j <= col_base*3+2):
                if i == row and j == col:
                    pass
                else:
                    for v in value:
                        try:
                            permutation.remove(v)
                        except KeyError:
                            pass
            if not len(permutation):
                break
        return permutation

    @staticmethod
    def list_possibility(num_board, i, j):
        choices = set([choice for choice in range(1, 10, 1)])
        for col in range(9):
            try:
                choices.remove(num_board[i][col])
            except KeyError:
                pass
        for row in range(9):
            try:
                choices.remove(num_board[row][j])
            except KeyError:
                pass
        row_base = i // 3
        col_base = j // 3
        for row in range(3):
            for col in range(3):
                try:
                    choices.remove(num_board[row_base*3 + row][col_base*3 + col])
                except KeyError:
                    pass
        return choices



a = Solution()
# board =       ["53..7....",
#                "6..195...",
#                ".98....6.",
#                "8...6...3",
#                "4..8.3..1",
#                "7...2...6",
#                ".6....28.",
#                "...419..5",
#                "....8..79"]
# a.solveSudoku(board)
# print(board)
print("####2####")
board2 = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
print(board2)
a.solveSudoku(board2)
print(board2)
