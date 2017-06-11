# https://leetcode.com/problems/perfect-squares/#/description

import random
import math

class Solution(object):
    def numSquares(self, n):
        sr = int(math.floor(math.sqrt(n)))
        squares = [i*i for i in range(1, sr+1)]
        dp = [None] * (n + 1)
        self.findMinList(dp, n, squares)
        #print(dp)
        return dp[n]

    def findMinList(self, dp, target, squares):
        if target == 0:
            return 0
        elif dp[target] is None:
            min_level = target
            for i in squares:
                if i <= target:
                    total_level = 1 + self.findMinList(dp, target - i, squares)
                    min_level = min(min_level, total_level)
                    # if min_level == 1:
                    #     break
                else:
                    break
            dp[target] = min_level
        return dp[target]

a = Solution()
print(a.numSquares(75))
for _ in range(0):
    print(random.randint(0, 20000))