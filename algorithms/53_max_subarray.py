# https://leetcode.com/problems/maximum-subarray/#/description


import random
class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return None
        storage = [0] * len(nums)
        storage[0] = nums[0]
        max_sum = storage[0]
        for i in range(1, len(nums)):
            storage[i] = nums[i] + (storage[i-1] if storage[i-1] > 0 else 0)
            max_sum = max(storage[i], max_sum)
        return max_sum

a = Solution()
a.maxSubArray([])

for _ in range(10):
    int_list = [random.randint(-10, 20) for _ in range(random.randint(0, 15))]
    print(int_list, a.maxSubArray(int_list))