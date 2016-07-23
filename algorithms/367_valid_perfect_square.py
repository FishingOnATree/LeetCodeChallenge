# https://leetcode.com/problems/valid-perfect-square/


class Solution(object):
    def isPerfectSquare(self, num):
        if num <= 0:
            return False
        else:
            sqrt = num ** 0.5
            return sqrt.is_integer()

valid_squares = set([i**2 for i in range(1, 1000)])
a = Solution()
for index in range(-5, 1000000):
    if a.isPerfectSquare(index) != (index in valid_squares):
        print("Error on number: ", index)