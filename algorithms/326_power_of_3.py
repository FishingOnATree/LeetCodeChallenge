# https://leetcode.com/problems/power-of-three/

import math

class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        else:
            power = int(math.log(n, 3))
        return (3 ** power) == n or (3 ** (power+1)) == n

a = Solution()
for ind in range(-10, 300):
    print(ind, a.isPowerOfThree(ind))