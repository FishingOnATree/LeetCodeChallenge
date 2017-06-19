# https://leetcode.com/problems/unique-paths-ii/#/description
import random

class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        if not len(grid) or not len(grid[0]) or grid[-1][-1] == 1 or grid[0][0] == 1:
            return 0
        row = len(grid)
        col = len(grid[0])
        marker = -1
        for r in range(row-1, -1, -1):
            for c in range(col-1, -1, -1):
                if grid[r][c] == 1:
                    grid[r][c] = marker
        grid[-1][-1] = 1
        obstacled = False
        for i in range(row-2, -1, -1):
            if grid[i][-1] == marker:
                obstacled = True
            if obstacled:
                grid[i][-1] = 0
            else:
                grid[i][-1] = 1
        obstacled = False
        for i in range(col-2, -1, -1):
            if grid[-1][i] == marker:
                obstacled = True
            if obstacled:
                grid[-1][i] = 0
            else:
                grid[-1][i] = 1
        for r in range(row-2, -1, -1):
            for c in range(col-2, -1, -1):
                if grid[r][c] < 0:
                    grid[r][c] = 0
                else:
                    grid[r][c] = grid[r+1][c] + grid[r][c+1]
        return grid[0][0]


a = Solution()
#print(a.uniquePathsWithObstacles([[0, 0, 0], [1, 0, 0], [0, 0, 0]]))
#print(a.uniquePathsWithObstacles([[0, 0, 0, 0], [0, 1, 0, 0]]))
#print(a.uniquePathsWithObstacles([[0, 0, 1], [0, 1, 0], [0, 0, 1]]))
#print(a.uniquePathsWithObstacles([[1, 0, 1], [0, 1, 0], [0, 0, 0]]))

for _ in range(20):
    r = random.randint(2, 10)
    c = random.randint(2, 10)
    la = [ [0]*c for _ in range(r)]
    for rn in range(r):
        for cn in range(c):
            if random.random() < 0.08:
                la[rn][cn] = 1
    print(la)