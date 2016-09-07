# https://leetcode.com/problems/sudoku-solver/
import copy
import collections


class Solution(object):
    def solveSudoku(self, board):
        num_board = []
        for row in board:
            num_board.append([0 if letter == "." else int(letter) for letter in row])
        length = len(board)
        solved, num_board = self.solve_sudoku(num_board, length)
        for i in range(length):
            board[i] = "".join([str(num_board[i][j]) for j in range(length)])

    def solve_sudoku(self, num_board, length):
        solved, possible_dict = self.solve_by_rule(num_board, length)
        if solved:
            return solved, num_board
        else:
            return self.permute_all(num_board, possible_dict, length)

    def permute_all(self, num_board, possible_dict, length):
        # order by length of choices
        ordered_dict = collections.OrderedDict(sorted(possible_dict.items(), key=lambda x: len(x[1])))
        for key, value in ordered_dict.items():
            for v in value:
                permutation_board = copy.deepcopy(num_board)
                permutation_board[key[0]][key[1]] = v
                try:
                    solved, result_board = self.solve_sudoku(permutation_board, length)
                    if solved:
                        return solved, result_board
                except Exception:
                    pass
        return False, None

    def solve_by_rule(self, num_board, length):
        solved = False
        stuck = False
        while not solved and not stuck:
            possible_dict = {}
            updated = False
            for i in range(length):
                for j in range(length):
                    if num_board[i][j] == 0:
                        possibility = self.list_possibility(num_board, i, j, length)
                        if len(possibility) == 0:
                            # throw exception
                            raise Exception("unsolvable")
                        elif len(possibility) == 1:
                            num_board[i][j] = possibility.pop()
                            updated = True
                        else:
                            possible_dict[tuple((i, j))] = possibility
            if len(possible_dict) == 0:
                solved = True
            elif not updated:
                for key, value in possible_dict.items():
                    row, col = key
                    possibility = self.list_permutation_possibility(possible_dict, row, col)
                    if len(possibility) == 1:
                        num_board[row][col] = possibility.pop()
                        updated = True
                if not updated:
                    #for key in sorted(list(possible_dict.keys())):
                    #    print(key, possible_dict[key])
                    stuck = True
                    break
        return solved, possible_dict

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
    def list_possibility(num_board, i, j, length):
        choices = set([choice for choice in range(1, len(num_board)+1, 1)])
        for col in range(length):
            try:
                choices.remove(num_board[i][col])
            except KeyError:
                pass
        for row in range(length):
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
board = ["6..5..4..", "789.....6", "...678...", "13..4..8.", "...321...", ".7..8..34", "...462...", "3.....621", "..8..3..7"]
print(board)
a.solveSudoku(board)
print(board)
print("####2####")
board2 = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
print(board2)
a.solveSudoku(board2)
print(board2)
print("####3####")
board3 = ["78.962..1","..1....7.",".5..17.3.",".981.6...","..5.3.8..","...7.931.",".3.62..9.",".6....4..","9..478.53"]
print(board3)
a.solveSudoku(board3)
print(board3)