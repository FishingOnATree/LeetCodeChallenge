# https://leetcode.com/problems/predict-the-winner/#/solutions

import random

class Solution(object):
    def PredictTheWinner(self, nums):
        self.cache = 0
        self.cal = 0
        storage = [[None] * len(nums) for _ in range(len(nums))]
        self.calculate(storage, nums, 0, len(nums) - 1)
        print(self.cache * 1.0 / (self.cache + self.cal))
        return storage[0][len(nums) - 1] >= 0

    def calculate(self, storage, nums, start, end):
        if storage[start][end] is None:
            self.cal += 1
            if start == end:
                storage[start][end] = nums[start]
            else:
                storage[start][end] = max(nums[start] - self.calculate(storage, nums, start+1, end), nums[end] - self.calculate(storage, nums, start, end - 1))
        else:
            self.cache +=1
        return storage[start][end]

a = Solution()
print(a.PredictTheWinner([1, 5, 2])) #false
print(a.PredictTheWinner([1, 5, 233, 7])) # true

for _ in range(10):
    nums = [random.randint(0, 10000) for _ in range(random.randint(3, 12))]
    print(a.PredictTheWinner(nums))