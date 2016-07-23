# https://leetcode.com/problems/sqrtx/
# 69

class Solution(object):
    def mySqrt(self, x):
        if x <= 0:
            return x
        else:
            return int(x ** 0.5)
