# https://leetcode.com/problems/container-with-most-water/

import random


class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0
        while right > left:
            max_area = max((right - left) * min(height[left], height[right]), max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


def correct_answer(heights):
    return max([min(heights[i], heights[j]) * (j-i) for i in range(len(heights) - 1) for j in range(i+1, len(heights))])


def generate_test(max_size, max_value):
    n = int(random.random() * (max_size - 5)) + 5
    return [int(random.random() * max_value) for _ in range(n)]

a = Solution()
for _ in range(10000):
    the_list = generate_test(100, 100)
    if (a.maxArea(the_list) != correct_answer(the_list)):
        print(the_list)
print("Finished")