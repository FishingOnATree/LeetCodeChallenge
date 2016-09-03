# https://leetcode.com/problems/triangle/

import random


class Solution(object):
    def minimumTotal(self, triangle):
        if len(triangle):
            sums = list(triangle[0])
            for index in range(1, len(triangle)):
                row = triangle[index]
                new_sums = [0] * len(triangle[index])
                new_sums[0] = row[0] + sums[0]
                for j in range(1, len(sums)):
                    new_sums[j] = row[j] + min(sums[j-1], sums[j])
                new_sums[-1] = sums[-1] + row[-1]
                sums = new_sums
                print(sums)
            return min(sums)
        else:
            return 0






MAX_VALUE = 50
a = Solution()
triangle = [[7], [47, 23], [11, 27, 4], [3, 44, 13, 12], [20, 50, 32, 19, 30], [36, 26, 17, 9, 20, 34], [45, 37, 27, 39, 16, 14, 26]]
print triangle
print a.minimumTotal(triangle)
for _ in range(-1):
    size = random.randint(0, 7)
    triangle = []
    for i in range(size):
        triangle.append([random.randint(0, MAX_VALUE) for _ in range(i+1)])
    print triangle
