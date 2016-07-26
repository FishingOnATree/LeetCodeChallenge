# https://leetcode.com/problems/divide-two-integers/
# Not solved yet because of the MAX_INT thing
import random
import sys

class Solution(object):
    def divide(self, signed_dividend, divisor):
        if divisor == 0:
            return sys.maxint
        else:
            num_negative_signs = 0
            if signed_dividend < 0:
                num_negative_signs += 1
            if divisor < 0:
                num_negative_signs += 1

            denom = abs(divisor)
            dividend = abs(signed_dividend)
            num_of_subtraction = 1
            answer = 0

            reminder = False
            if denom > dividend:
                answer = 0
                reminder = dividend > 0
            elif denom == dividend:
                answer = 1
            else:
                while denom <= dividend:
                    denom <<= 1
                    num_of_subtraction <<= 1

                denom >>= 1
                num_of_subtraction >>= 1
                while num_of_subtraction != 0:
                    if dividend >= denom:
                        dividend -= denom
                        answer |= num_of_subtraction
                    num_of_subtraction >>= 1
                    denom >>= 1
                reminder = dividend > 0
            if num_negative_signs == 1:
                answer *= -1
                if reminder:
                    answer -= 1 # floor integer division
                if answer < -sys.maxint-1:
                    answer = -sys.maxint-1
            else:
                if answer > sys.maxint:
                    answer = sys.maxint
            return answer

a = Solution()
max = sys.maxint
print("-2147483648/ -1 =", a.divide(-2147483648, -1))
for _ in range(10000):
    product = 1 if random.random() < 0.5 else -1
    m = int(random.random() * (max - 1) * product)
    product = 1 if random.random() < 0.5 else -1
    n = int(random.random() * (max - 1) * product)
    if m/n != a.divide(m, n):
        print("Failed on :", m, " divides", n)
print("Done")
