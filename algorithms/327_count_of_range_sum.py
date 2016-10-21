# https://leetcode.com/problems/count-of-range-sum/


# class Bit:
#     def __init__(self, n):
#         sz = 1
#         while n >= sz:
#             sz *= 2
#         self.size = sz
#         self.data = [0]*sz
#
#     def sum(self, i):
#         assert i > 0
#         s = 0
#         while i > 0:
#             s += self.data[i]
#             i -= i & -i
#         return s
#
#     def add(self, i, x):
#         assert i > 0
#         while i < self.size:
#             self.data[i] += x
#
import random

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        if not nums:
            return 0
        else:
            n = len(nums)
            sum_array = []
            total = 0
            for i, x in enumerate(nums):
                sum_array.append([total, i])
                total += x
            sum_array.append([total, n])
            index_array = sorted(list(sum_array), key=lambda x: x[0])
            ans = 0
            for a in range(n, 0, -1):
                left_pos = bisect_left(sum_array, lower - sum_array[a][0])
                right_pos = bisect_right(sum_array, upper - sum_array[a][0])
                for i in range(left_pos, right_pos):
                    if sum_array[i][1] <= a - 1:
                        ans += 1
                if lower <= sum_array[a][0] - sum_array[a-1][0] <= upper:
                    ans += 1
            return ans


def bisect_left(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid][0] < x: lo = mid+1
        else: hi = mid
    return lo


def bisect_right(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid][0]: hi = mid
        else: lo = mid+1
    return lo


def generate_test(n, max_value, min_value):
    size = random.randint(5, n)
    test_list = [0] * size
    for i in range(size):
        test_list[i] = random.randint(min_value, max_value)
    p1 = random.randint(min_value/2, max_value/2)
    p2 = random.randint(min_value/2, max_value/2)
    return test_list, min(p1, p2), max(p1, p2)


a = Solution()
print(a.countRangeSum([84, 165, 163, 103, 73, 13, -46, -44, 79, 26, 200, 156, 108, -23, 43, 75, 28, 135, 117, -37, -43, 149, 76, 173, 73, 124, 19, -6], -12, 84))
for _ in range(0):
    test_list, lower, upper = generate_test(30, 200, -50)
    print(test_list)
    print(lower)
    print(upper)
