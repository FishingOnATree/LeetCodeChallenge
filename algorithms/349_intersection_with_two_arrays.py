# https://leetcode.com/problems/intersection-of-two-arrays/

import random

class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))


def generate_test(size, max_value):
    return_list = []
    for _ in range(size):
        value = int(max_value * random.random())
        return_list.append(value)
    return return_list
print(generate_test(10000, 1000000))
print(generate_test(10000, 1000000))