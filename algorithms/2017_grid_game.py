from typing import List

class Solution:

    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        # robot A - goal is to minimize the score of Robot B, NOT maximize its own score.
        # print("ROBOT A ----------------------------------------\n\n ")
        # print("Grid: ", grid)
        pre_computed = self.precomute_robot_a_grid(grid, n)
        # print("pre_comuted: ", pre_computed)
        self.robot_a_move(grid, n, pre_computed)
        # robot B
        # print("ROBOT B ----------------------------------------\n\n ")
        # print("Grid: ", grid)
        pre_computed = self.precomute_robot_b_grid(grid, n)
        # print("pre_comuted: ", pre_computed)
        points = self.robot_b_move(grid, n, pre_computed)
        return points

    def robot_a_move(self, grid, n, pre_computed):
        # robot 1
        pivot = -1
        max_points = None
        for i in range(0, n):
            # print("iteration: ", i, " - ", pre_computed[0][i+1] if i+1 < n else 0 , " - ", pre_computed[1][i-1] if i-1 >= 0 else 0)
            #max_pt_step = max(pre_computed[0][i+1] if i+1 < n else 0, pre_computed[1][i-1] - pre_computed[1][i] if i-1 >= 0 else pre_computed[1][i])
            max_pt_step = max(pre_computed[0][i+1] if i+1 < n else 0, pre_computed[1][i-1] if i-1 >= 0 else 0)
            if max_points == None or max_pt_step < max_points:
                pivot = i
                max_points = max_pt_step #new min
        # print("max_points: ", max_points)
        # print("pivot: ", pivot)
        for x in range(0, pivot+1):
            grid[0][x] = 0
        for x in range(pivot, n):
            grid[1][x] = 0
        # print("Grid after A moved: ", grid)

    def robot_b_move(self, grid, n, pre_computed):
        # robot 1:
        x = 1
        y = n - 1
        points = grid[x][y]
        grid[x][y] = 0
        # count = 0
        while x != 0:
            # print("({},{}): {} vs {} ".format(x, y, pre_computed[x - 1][y], grid[x][y - 1] + pre_computed[x][y - 1]))
            if (y > 0 and pre_computed[x - 1][y] > (grid[x][y - 1] + pre_computed[x - 1][y - 1]) and pre_computed[x - 1][y] > pre_computed[x][y-1]) or y == 0:  # move up
                points += pre_computed[x - 1][y]
                x = 0
                for i in range(y, -1, -1):
                    grid[x][i] = 0
            else:
                points += grid[x][y - 1]
                grid[x][y - 1] = 0
                y -= 1
            # count += 1
            # print("Grid iteration: ", count, grid)
        # print("Final grid: ", grid)
        return points

    def precomute_robot_a_grid(self, grid, n):
        pre_computed = [[0] * n, [0] * n]
        pre_computed[0][n-1] = grid[0][n-1]
        pre_computed[1][0] = grid[1][0]
        for i in range(1, n-1):
            pre_computed[0][n-i-1] = grid[0][n-i-1] + pre_computed[0][n-i]
            pre_computed[1][i] = grid[1][i] + pre_computed[1][i-1]
        if n > 1:
            pre_computed[1][n-1] = pre_computed[1][n-2]
        return pre_computed


    def precomute_robot_b_grid(self, grid, n):
        pre_computed = [[0] * n, [0] * n]
        pre_computed[0][0] = grid[0][0]
        pre_computed[1][0] = grid[0][0] + grid[1][0]
        for i in range(1, n):
            pre_computed[0][i] = grid[0][i] + pre_computed[0][i - 1]
            pre_computed[1][i] = grid[1][i] + pre_computed[1][i - 1] if pre_computed[1][i-1] > pre_computed[0][i] else pre_computed[0][i]
        return pre_computed


solution = Solution()
# print(solution.gridGame([[2,5,4],[1,5,1]]))
print(solution.gridGame([[4, 9, 3], [7, 9, 5]]))
print(solution.gridGame([[10, 5, 5, 3, 10, 5, 8], [9, 1, 10, 4, 2, 4, 9]]))

import random

MAX = 100
N_MAX = 10

for i in range(5):
    n = random.randint(1, N_MAX)
    a = list()
    a.append([random.randint(1, MAX) for _ in range(n)])
    a.append([random.randint(1, MAX) for _ in range(n)])
    print(a)
