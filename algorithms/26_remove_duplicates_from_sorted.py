# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

import random


class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums):
            j = 1
            for i in range(1, len(nums)):
                if nums[i] != nums[i-1]:
                    nums[j] = nums[i]
                    j += 1
            return j
        else:
            return 0

MAX_VALUE = 50
a = Solution()
print(a.removeDuplicates([]))
print(a.removeDuplicates([1]))
for _ in range(10):
    size = random.randint(0, 20)
    nums = [random.randint(0, MAX_VALUE) for _ in range(size)]
    nums.sort()
    print nums
