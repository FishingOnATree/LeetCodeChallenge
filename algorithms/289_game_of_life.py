import random

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        else:
            row_len, col_len = len(board), len(board[0])
            score = [[0] * col_len for _ in range(row_len)]
            for row in range(row_len):
                for col in range(col_len):
                    score[row][col] = sum([board[i][j] for i in range(max(row-1, 0), min(row+2, row_len)) for j in range(max(col-1, 0), min(col+2, col_len))]) - board[row][col]
            print score
            for row in range(row_len):
                for col in range(col_len):
                    board[row][col] = 1 if score[row][col] == 3 or board[row][col] + score[row][col] == 3 else 0
        # can use 2-bits to represent states for no extra space cost, but it would slow down.

a = Solution()
board = [[0, 1, 0], [1, 0, 1], [1, 1, 1]]
print(board)
a.gameOfLife(board)
print(board)

for _ in range(10):
    row = random.randint(1, 20)
    col = random.randint(1, 20)
    a_list = [[0 if random.random() < 0.5 else 1 for _ in range(col)] for _ in range(row)]
    print(a_list)