# https://leetcode.com/problems/minimum-path-sum/#/description

import random

class Solution(object):
    def minPathSum(self, grid):
        if not len(grid) or not len(grid[0]):
            return 0
        row = len(grid)
        col = len(grid[0])
        cost = [[0] * col for _ in range(row)]
        cost[-1][-1] = grid[-1][-1]
        for i in range(row-2, -1, -1):
            cost[i][-1] = cost[i+1][-1] + grid[i][-1]
        for i in range(col-2, -1, -1):
            cost[-1][i] = cost[-1][i+1] + grid[-1][i]
        for r in range(row-2, -1, -1):
            for c in range(col-2, -1, -1):
                cost[r][c] = min(cost[r+1][c], cost[r][c+1]) + grid[r][c]
        return cost[0][0]

a = Solution()
a.minPathSum([[1, 2, 3], [1, 2, 3], [1, 2, 3]])

for _ in range(10):
    r = random.randint(2, 5)
    c = random.randint(2, 5)
    la = [ [0]*c for _ in range(r)]
    for rn in range(r):
        for cn in range(c):
            la[rn][cn] = random.randint(0, 10)
    print(la)