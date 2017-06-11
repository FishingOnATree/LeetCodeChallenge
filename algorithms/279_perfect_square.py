# https://leetcode.com/problems/perfect-squares/#/description

import random
import time
import math
import bisect

class Solution(object):
    def numSquares(self, n):
        sr = int(math.floor(math.sqrt(n)))
        squares = [i*i for i in range(1, sr+1)]
        dp = [None] * (n + 1)
        self.findMinList(dp, n, squares)
        return dp[n]

    def findMinList(self, dp, target, squares):
        if dp[target] is None:
            min_level = target
            index = bisect.bisect(squares, target) - 1
            for k in range(index, -1, -1):
                i = squares[k]
                if i == target:
                    min_level = 1
                    break
                elif i < target:
                    total_level = 1 + self.findMinList(dp, target - i, squares)
                    min_level = min(min_level, total_level)
                    if min_level == 2:
                        break
            dp[target] = min_level
        return dp[target]

a = Solution()
start_time = time.time()
answer = a.numSquares(3461) #2  0.079 sec
print("--- %s seconds ---" % (time.time() - start_time))
print(answer)
for _ in range(0):
    print(random.randint(0, 10000))