# https://leetcode.com/problems/4sum/

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

a = Solution()
assert(set(a.fourSum([1, 0, -1, 0, -2, 2])) ==
        ([
          [-1,  0, 0, 1],
          [-2, -1, 1, 2],
          [-2,  0, 0, 2]
        ]))
