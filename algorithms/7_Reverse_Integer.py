# https://leetcode.com/problems/reverse-integer/

#
# class Solution(object):
#     def reverse(self, x):
#         product = 1 if x >= 0 else -1
#         a = abs(x)
#         b = 0
#         while a != 0:
#             b *= 10
#             b = b + a%10
#             a //= 10
#         result = b * product
#         bound = pow(2, 31)
#         if  (bound * -1) <= result <= bound - 1:
#             return result
#         else:
#             return 0
#

class Solution(object):
    def reverse(self, x):
        product = 1 if x >= 0 else -1
        a = abs(x)
        result = int(str(a)[::-1]) * product
        bound = pow(2, 31)
        if  (bound * -1) <= result <= bound - 1:
            return result
        else:
            return 0


a = Solution()
print(a.reverse(0))
print(a.reverse(123))
print(a.reverse(3))
print(a.reverse(-213))
print(a.reverse(-231))
print(a.reverse(1534236469))
print(a.reverse(2147483641))
print(pow(2, 31) - 1)