# 167: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

import random


import bisect

class Solution(object):
    def twoSum(self, numbers, target):
        lo = 0
        hi = bisect.bisect_right(numbers, target)
        if hi == len(numbers):
            hi -= 1
        while hi > 0:
            new_target = target-numbers[hi]
            lower_index = bisect.bisect_left(numbers, new_target, hi=hi-1)
            if new_target == numbers[lower_index]:
                return [lower_index+1, hi+1]
            else:
                hi -= 1
        return None


a = Solution()
print(a.twoSum([0, 0, 3, 4], 0))
print(a.twoSum([1, 2, 3, 4, 7], 11))
print(a.twoSum([1, 2, 3, 4, 7], 3))
print(a.twoSum([1, 2, 3, 4, 7], 4))
print(a.twoSum([1, 2, 3, 4, 7], 6))

