__author__ = 'Rays'
class Solution(object):
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + int((end-start)/2)
            #print(start, mid, end)
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[end]:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1


a = Solution()
print(a.search([3, 4, 5, 6, 0, 1, 2], 3))
print(a.search([3, 4, 5, 6, 0, 1, 2], 2))
print(a.search([3, 4, 5, 6, 0, 1, 2], -1))
print(a.search([3, 4, 5, 6, 0, 1, 2], 0))