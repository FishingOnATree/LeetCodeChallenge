__author__ = 'Rays'
# https://leetcode.com/problems/burst-balloons/#/description
# DP to try all possible scenarios

import random

class Solution(object):
    def maxCoins(self, nums):
        self.my_dict = {}
        return self.findMax(nums)

    def findMax(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        key = tuple(nums)
        if key not in self.my_dict:
            max_coins = 0
            for i in range(len(nums)):
                new_nums = list(nums)
                new_nums.pop(i)
                curr = self.getValue(i - 1, nums) * nums[i] * self.getValue(i+1, nums) + self.findMax(new_nums)
                #print(i, self.getValue(i - 1, nums), nums[i], self.getValue(i+1, nums), self.getValue(i - 1, nums) * nums[i] * self.getValue(i+1, nums))
                max_coins = max(max_coins, curr)
            self.my_dict[key] = max_coins
            # print(key, max_coins)
        return self.my_dict[key]

    def getValue(self, i, nums):
        return nums[i] if 0 <= i <= len(nums) - 1 else 1

a = Solution()
#print(a.maxCoins([3, 5, 8])) #152
print(a.maxCoins([3, 1, 5, 8])) #167
# print(a.maxCoins([1,2,3,4,5,6,7,8])) #912
for _ in range(10):
    print([random.randint(0, 100) for _ in range(random.randint(5, 15))])