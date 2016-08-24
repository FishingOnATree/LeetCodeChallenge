# https://leetcode.com/problems/jump-game/
import random


class Solution(object):
    def canJump(self, nums):
        n = len(nums)
        max_index_reached = 0
        count = 0
        while count < n and count <= max_index_reached:
            max_index_reached = max(nums[count] + count, max_index_reached)
            count += 1
        return max_index_reached >= n - 1

a = Solution()
print(a.canJump([4, 0, 0, 0, 0]))
print(a.canJump([4, 0, 0, 0, 0, 1]))
for _ in range(10):
    size = random.randint(3, 25)
    print([0 if random.random() > 0.45 else random.randint(1, 5) for _ in range(size)])
