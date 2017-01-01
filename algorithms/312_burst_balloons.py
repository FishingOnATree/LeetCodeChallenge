__author__ = 'Rays'



class Solution(object):
    def maxCoins(self, nums):
        #greedy algorithm that always remove smallest int -- doesn't work
        total = 0
        for _ in range(len(nums)):
            # find min
            index = 0
            for i in range(1, len(nums)):
                if nums[i] < nums[index]:
                    index = i
            left = nums[index-1] if index-1 >= 0 else 1
            right = nums[index+1] if index+1 < len(nums) else 1
            total += left * nums[index] * right
            nums.pop(index)
        return total


a = Solution()
print(a.maxCoins([3, 1, 5, 8])) #167

print(a.maxCoins([1,2,3,4,5,6,7,8])) #912