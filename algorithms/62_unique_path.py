# https://leetcode.com/problems/unique-paths/#/description

import random

class Solution(object):
    def uniquePaths(self, row, col):
        if not row or not col:
            print("here")
            return 0
        cost = [[0] * col for _ in range(row)]
        cost[-1][-1] = 1
        for i in range(row-2, -1, -1):
            cost[i][-1] = 1
        for i in range(col-2, -1, -1):
            cost[-1][i] = 1
        for r in range(row-2, -1, -1):
            for c in range(col-2, -1, -1):
                cost[r][c] = cost[r+1][c] + cost[r][c+1]
        return cost[0][0]

a = Solution()
print(a.uniquePaths(1, 1))
for _ in range(0):
    r = random.randint(3, 15)
    print(r)
    c = random.randint(3, 15)
    print(c)