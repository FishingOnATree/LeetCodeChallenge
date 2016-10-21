# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
import random


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """


for _ in range(5000):
    rows = random.randint(1, 10)
    cols = random.randint(1, 10)
    a_list = [random.randint(-500, 1500) for _ in range(rows * cols)]
    a_list.sort()
    final_list = []
    for r in range(rows):
        item = [a_list[r*cols + c] for c in range(cols)]
        final_list.append(item)
    if random.random() < 0.5:
        target = random.randint(-500, 1500)
    else:
        target = a_list[random.randint(0, len(a_list)-1)]
    # if a.searchMatrix(final_list, target) != a.searchMatrix2(final_list, target):
    #     print "****ERROR****"
    #     print final_list
    #     print target