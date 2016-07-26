# https://leetcode.com/problems/3sum/

import random


class Solution(object):
    def threeSum(self, nums):
        return_list = []
        target = 0
        num_list = sorted(nums)
        n = len(num_list)
        for i in range(n-2):
            if i > 0 and num_list[i] == num_list[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                sum = num_list[i] + num_list[l] + num_list[r]
                if sum == target:
                    return_list.append([num_list[i], num_list[l], num_list[r]])
                    l += 1
                    while l < n and num_list[l] == num_list[l-1]:
                        l += 1
                    r -= 1
                    while r >= 0 and num_list[r] == num_list[r+1]:
                        r -= 1
                elif sum > target:
                    r -= 1
                else:
                    l += 1
        return return_list


def generate_test(max_size, max_value):
    n = int(random.random() * (max_size-10)) + 10
    the_list = []
    for _ in range(n):
        value = int(random.random() * max_value)
        value *= 1 if random.random() > 0.3 else -1
        the_list.append(value)
    return the_list


a = Solution()
print(a.threeSum([2, 10, 9, -5, 17, 15, 17, -18, 17, 17, -9, -19, 10, 2, 2, 10, 17, -2, -16, 0, 19, -17, 6]))
print(a.threeSum([0, 0, 0]))
count = 0
for i in range(count):
    print(generate_test(30, 20))