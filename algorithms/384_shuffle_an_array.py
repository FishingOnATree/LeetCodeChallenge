# https://leetcode.com/problems/shuffle-an-array/

import random


class Solution(object):

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return list(self.nums)

    def shuffle(self):
        size = len(self.nums)
        from_list = list(self.nums)
        return_list = [0] * size
        for n in range(size, 1, -1):
            index = random.randint(0, n-1)
            return_list[size - n] = from_list.pop(index)
        if len(from_list):
            return_list[-1] = from_list.pop(0)
        return return_list


# Your Solution object will be instantiated and called as such:
obj = Solution([])
count_dict = {}
for _ in range(1):
    param_2 = tuple(obj.shuffle())
    count_dict.setdefault(param_2, 0)
    count_dict[param_2] += 1
print(count_dict)