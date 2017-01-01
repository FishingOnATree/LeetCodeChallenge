# https://leetcode.com/problems/battleships-in-a-board/

class Solution(object):
    def countBattleships(self, board):
        total = 0
        for row_idx in range(len(board)):
            for col_idx in range(len(board[row_idx])):
                if board[row_idx][col_idx] == 'X':
                    total += 1
                    self.convertX(row_idx, col_idx, board)
        return total

    def convertX(self, row_idx, col_idx, board):
        board[row_idx][col_idx] = 'O'
        if len(board) > row_idx + 1 and board[row_idx+1][col_idx] == 'X':
            next_row = row_idx+1
            while next_row < len(board) and board[next_row][col_idx] == 'X':
                board[next_row][col_idx] = 'O'
                next_row += 1
        elif len(board[row_idx]) > col_idx+1 and board[row_idx][col_idx+1] == 'X':
            next_col = col_idx + 1
            while next_col < len(board[row_idx]) and board[row_idx][next_col] == 'X':
                board[row_idx][next_col] = 'O'
                next_col += 1


def generate_board(row_len, col_len):
    board = ["." * col_len for _ in range(row_len)]
    print(board)

print(generate_board(5, 10))
