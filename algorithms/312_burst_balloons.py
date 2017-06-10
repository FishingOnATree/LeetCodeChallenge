__author__ = 'Rays'
# https://leetcode.com/problems/burst-balloons/#/description
# DP to try all possible scenarios

import random
import time

class Solution(object):
    def maxCoins(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        else:
            storage = [[-1] * len(nums) for _ in range(len(nums))]
            self.findMax(nums, storage)
            return storage[0][len(nums) - 1]

    def findMax(self, nums, storage):
        for range_len in range(1, len(nums) + 1):
            for range_start in range(0, len(nums) - range_len + 1):
                range_end = range_start + range_len - 1
                for k in range(range_start, range_end + 1):
                    # assume nums[k] is the last one to remove within (range_start, range_end), so the formula becomes d
                    coins = self.getValue(range_start-1, nums) * nums[k] * self.getValue(range_end+1, nums)
                    left_max = 0 if k == range_start else storage[range_start][k-1]
                    right_max = 0 if k == range_end else storage[k+1][range_end]
                    storage[range_start][range_end] = max(storage[range_start][range_end], coins+left_max+right_max)

    def getValue(self, i, nums):
        return nums[i] if 0 <= i <= len(nums) - 1 else 1

#print(a.maxCoins([3, 5, 8])) #152
#print(a.maxCoins([3, 1, 5, 8])) #167
#print(a.maxCoins([1,2,3,4,5,6,7,8])) #912
#nums = [94, 11, 95, 56, 90, 58, 18, 44, 21, 1, 78, 15, 50, 3, 68, 15, 50, 68, 5] # 4348328, 11+sec
#nums = [94, 11, 95, 56, 90, 58, 18, 44, 21, 1, 78, 15, 50, 3, 68, 15, 50] # 3974342, 2.632sec
#print(a.maxCoins(nums)) # 4348328
a = Solution()
nums = [94, 11, 95, 56, 90, 58, 18, 44, 21, 1, 78, 15, 50, 3, 68, 15, 50, 68, 5]
start_time = time.time()
answer = a.maxCoins(nums)
print("--- %s seconds ---" % (time.time() - start_time))
print(answer)

for _ in range(0):
    print([random.randint(0, 100) for _ in range(50)])