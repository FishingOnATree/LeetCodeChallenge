# https://leetcode.com/problems/reverse-integer/


class Solution(object):
    def reverse(self, x):
        product = 1 if x >= 0 else -1
        a = abs(x)
        b = 0
        while a != 0:
            rem = a % 10
            b += rem
            if a > 10:
                b *= 10
            a /= 10
        if type(b * product) == long:
            return 0
        else:
            return b * product

a = Solution()
print(a.reverse(0))
print(a.reverse(123))
print(a.reverse(3))
print(a.reverse(-213))
print(a.reverse(-231))
print(a.reverse(1534236469))