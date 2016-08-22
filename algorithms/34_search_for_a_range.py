# https://leetcode.com/problems/search-for-a-range/

import bisect


class Solution(object):
    def searchRange(self, nums, target):
        index = bisect.bisect_left(nums, target)
        size = len(nums)
        if index < size and nums[index] == target:
            end_index = index + 1
            while end_index < size and nums[end_index] == target:
                end_index += 1
            return[index, end_index - 1]
        else:
            return [-1, -1]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

a = Solution()
print(a.searchRange([5, 7, 7, 8, 8, 10], 8))
print(a.searchRange([5, 7, 7, 8, 10], 8))
print(a.searchRange([5, 7, 7, 8, 10], 10))
print(a.searchRange([5, 7, 7, 8, 10], 4))
print(a.searchRange([5, 7, 7, 8, 10], 11))