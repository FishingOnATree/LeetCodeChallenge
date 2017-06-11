# https://leetcode.com/problems/range-sum-query-immutable/#/description


class NumArray(object):

    def __init__(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        self.nums = nums

    def sumRange(self, i, j):
        return self.nums[j] if i == 0 else self.nums[j] - self.nums[i-1]

a = NumArray([1,1,1,1,1,1])
print(a.sumRange(0, 2))
print(a.sumRange(2, 5))
print(a.sumRange(0, 5))
print(a.sumRange(5, 5))