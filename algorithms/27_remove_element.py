# https://leetcode.com/problems/remove-element/

import random


class Solution(object):
    def removeElement(self, nums, val):
        tail = len(nums) - 1
        head = 0
        while head <= tail:
            if nums[head] == val:
                tmp = nums[tail]
                nums[tail] = nums[head]
                nums[head] = tmp
                tail -= 1
            else:
                head += 1
        return head




MAX_VALUE = 50
a = Solution()
for _ in range(10):
    size = random.randint(0, 20)
    nums = [random.randint(0, MAX_VALUE) for _ in range(size)]
    target = random.randint(0, MAX_VALUE)
    print nums
    print target
