# https://leetcode.com/problems/two-sum/
import math
import random

class Solution(object):
    def twoSum(self, nums, target):
        the_dict = {}
        for index, n in enumerate(nums):
            partner = target - n
            if n in the_dict:
                return [the_dict[n], index]
            else:
                the_dict[partner] = index
        return []


def generate_test(max_size, max_value):
    n = int(random.random() * (max_size-10)) + 10
    the_list = []
    for _ in range(n):
        value = - 1
        while value in the_list or value == -1:
            value = int(random.random() * max_value)
        the_list.append(value)
    n1 = int(random.random() * n)
    n2 = int(random.random() * n)
    if n1 == n2:
        if n2 + 1 < n:
            n2 += 1
        else:
            n1 -= 1
    target = the_list[n1] + the_list[n2]
    return the_list, target, sorted([n1, n2])

a = Solution()
assert(a.twoSum([1, 3, 5, 7], 6) == [0, 2])
count = 1000
for _ in range(count):
    the_list, the_target, the_answer = generate_test(14, 10000)
    if a.twoSum(the_list, the_target) != the_answer:
        print(the_list, the_target, the_answer, a.twoSum(the_list, the_target))