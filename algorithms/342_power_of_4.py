# https://leetcode.com/problems/power-of-four/
import math

class Solution(object):
    def isPowerOfFour(self, num):
        if num <= 0:
            return False
        else:
            power = int(math.log(num, 4))
        return (4 ** power) == num or (4 ** (power+1)) == num

a = Solution()
for ind in range(-10, 300):
    print(ind, a.isPowerOfFour(ind))