import random

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        row_set = set()
        col_set = set()
        col_len = len(matrix[0])
        for row in range(len(matrix)):
            for col in range(col_len):
                if matrix[row][col] == 0:
                    row_set.add(row)
                    col_set.add(col)
        for row in row_set:
            matrix[row] = [0] * col_len
        for row in range(len(matrix)):
            for col in col_set:
                matrix[row][col] = 0
a = Solution()
a.setZeroes([[85, 89, 19, 93, 10, 66, 19, 70, 22, 93, 80, 15], [49, 3, 42, 3, 91, 78, 68, 67, 0, 77, 5, 92], [65, 98, 12, 93, 95, 30, 10, 94, 93, 58, 42, 78], [77, 23, 47, 56, 81, 68, 21, 52, 32, 29, 44, 48], [86, 71, 58, 19, 94, 56, 63, 44, 14, 29, 45, 45], [78, 19, 91, 60, 76, 16, 74, 89, 87, 37, 39, 69], [83, 20, 6, 55, 99, 38, 9, 33, 61, 76, 69, 79], [12, 29, 25, 30, 84, 43, 53, 15, 65, 19, 2, 81], [34, 41, 64, 51, 65, 39, 10, 17, 62, 12, 21, 7], [7, 13, 26, 12, 10, 81, 25, 91, 70, 50, 56, 39], [28, 6, 26, 40, 19, 16, 14, 97, 9, 70, 48, 34], [23, 1, 6, 49, 67, 64, 34, 38, 70, 13, 52, 59], [36, 96, 32, 32, 36, 26, 100, 34, 83, 78, 77, 55], [0, 25, 67, 73, 24, 72, 26, 83, 29, 40, 67, 2], [19, 49, 18, 55, 70, 60, 16, 94, 39, 3, 56, 24], [26, 17, 20, 81, 78, 85, 66, 57, 18, 38, 49, 52], [67, 26, 0, 1, 11, 26, 20, 88, 41, 97, 30, 41]])


for _ in range(10):
    row_len = random.randint(10, 20)
    col_len = random.randint(10, 20)
    board = [[random.randint(0, 100) for _ in range(col_len)] for _ in range(row_len)]
    print board