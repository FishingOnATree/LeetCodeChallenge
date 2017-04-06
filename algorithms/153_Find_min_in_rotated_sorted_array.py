__author__ = 'Rays'
# Leetcode 153: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/#/description

class Solution(object):
    def findMin(self, nums):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + int((end-start)/2)
            #print(start, mid, end)
            if nums[start] > nums[end] and nums[mid] > nums[start]:
                start = mid
            else:
                end = mid
        return  nums[start] if nums[start] < nums[end] else nums[end]

a = Solution()
print(a.findMin([3, 4, 5, 6, 0, 1, 2]))
print(a.findMin([3, 4, 5, 6, 7, 1, 2]))
print(a.findMin([3, 4, 5, 6]))
print(a.findMin([3, 4, 5, 6, 7, 1]))
print(a.findMin([9, 3, 4, 5, 6, 7, 8]))
print(a.findMin([9, 10, 3, 4, 5, 6, 7, 8]))