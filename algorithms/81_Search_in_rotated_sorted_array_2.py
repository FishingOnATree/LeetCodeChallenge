# Leetcode #81 https://leetcode.com/problems/search-in-rotated-sorted-array-ii/#/description
__author__ = 'Rays'

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + int((end-start)/2)
            #print(start, mid, end)
            if nums[mid] == target:
                return True
            if nums[mid] < nums[end]:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            elif nums[mid] > nums[end]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                end -= 1
        return False

a = Solution()
print(a.search([3, 1, 1], 3))
print(a.search([1, 1, 3], 3))
print(a.search([1, 1, 3, 1], 3))
