# https://leetcode.com/problems/search-a-2d-matrix/


import random
import bisect

class Solution(object):

    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        if not rows:
            return False
        else:
            cols = len(matrix[0])
            if not cols:
                return False
            low, high = 0, rows-1
            found = False
            while not found and low < high:
                row = (high + low)/2
                if matrix[row][0] <= target <= matrix[row][-1]:
                    found = True
                elif target > matrix[row][-1]:
                    low = row + 1
                else:
                    high = row
            if not found and matrix[high][0] <= target <= matrix[high][-1]:
                found = True
                row = high
            if found:
                print(matrix[row])
                pos = bisect.bisect_left(matrix[row], target)
                print(matrix[row][pos])
                return matrix[row][pos] == target
            else:
                return False

a = Solution()
print a.searchMatrix([[]], 1)
# matrix = [[1,   3,  5,  7],
#           [10, 11, 16, 20],
#           [23, 30, 34, 50]]
# print a.searchMatrix(matrix, -1)
# print a.searchMatrix(matrix, 1)
# print a.searchMatrix(matrix, 8)
# print a.searchMatrix(matrix, 24)
# print a.searchMatrix(matrix, 23)
# print a.searchMatrix(matrix, 30)
# print a.searchMatrix(matrix, 50)
# for _ in range(50):
#     rows = random.randint(1, 10)
#     cols = random.randint(1, 10)
#     a_list = [random.randint(-500, 1500) for _ in range(rows * cols)]
#     a_list.sort()
#     final_list = []
#     for r in range(rows):
#         item = [a_list[r*cols + c] for c in range(cols)]
#         final_list.append(item)
#     if random.random() < 0.5:
#         target = random.randint(-500, 1500)
#     else:
#         target = a_list[random.randint(0, len(a_list)-1)]
#     print final_list
#     print target