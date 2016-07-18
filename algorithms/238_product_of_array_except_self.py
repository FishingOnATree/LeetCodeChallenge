# https://leetcode.com/problems/product-of-array-except-self/
# O(n), no division
# For example, given [1,2,3,4], return [24,12,8,6]


class Solution(object):
    def productExceptSelf(self, nums):
        total = 1
        num_of_zeros = 0
        for n in nums:
            if n == 0:
                num_of_zeros += 1
            else:
                total *= n

        if num_of_zeros >= 2:
            result = [0] * len(nums)
        elif num_of_zeros == 1:
            result = [0 if n != 0 else total for n in nums]
        else:
            result = [self.divide_by_shift(total, n) for n in nums]
        return result

    def divide_by_shift(self, signed_dividend, divisor):
            num_negative_signs = 0
            if signed_dividend < 0:
                num_negative_signs += 1
            if divisor < 0:
                num_negative_signs += 1

            denom = abs(divisor)
            dividend = abs(signed_dividend)
            num_of_subtraction = 1
            answer = 0

            if denom > dividend:
                answer = 0
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
            if num_negative_signs == 1:
                answer *= -1
            return answer


a = Solution()

# print(a.productExceptSelf([1, -1]))

assert (a.productExceptSelf([1, -1]) == [-1, 1])
assert (a.productExceptSelf([5, -5, 5, -5]) == [125, -125, 125, -125])
assert (a.productExceptSelf([1,2,3,4]) == [24,12,8,6])
assert (a.productExceptSelf([0,2,3]) == [6,0,0])
assert (a.productExceptSelf([0, 0, 1, 2, 3]) == [0,0,0,0,0])
