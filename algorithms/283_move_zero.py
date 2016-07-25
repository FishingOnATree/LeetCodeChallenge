# https://leetcode.com/problems/move-zeroes/
import random


class Solution(object):
    def moveZeroes(self, nums):
        index = 0
        count = 0
        while count < len(nums):
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
            else:
                index += 1
            count += 1


def generate_test(size, max_value):
    return_list = []
    for _ in range(size):
        if random.random() < 0.3:
            value = 0
        else:
            value = int(max_value * random.random())
        return_list.append(value)
    return return_list

a = Solution()
nums = [0, 1, 0, 3, 12]
a.moveZeroes(nums)
print(nums)
assert(nums == [1, 3, 12, 0, 0])
for index_ in range(20):
    the_list = generate_test(15, 30)
    the_list_copy = list(the_list)
    a.moveZeroes(the_list)
    print(index_, the_list_copy, the_list)
    #print(the_list_copy)