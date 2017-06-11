# https://leetcode.com/problems/guess-number-higher-or-lower-ii/#/description

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        else:
            nums = [n for n in range(1, n+1)]
            storage = [[None] * n for _ in range(n)]
            for i in range(n):
                storage[i][i] = 0
            self.findMin(nums, 0, n-1, storage)
            return storage[0][n-1]

    def findMin(self, nums, start, end, storage):
        #print(nums, start, end)
        if storage[start][end] is None:
            if start + 1 == end:
                storage[start][end] = nums[start]
            elif start + 2 == end:
                storage[start][end] = nums[start+1]
            else:
                min_value = nums[start] + self.findMin(nums, start+1, end, storage)
                for i in range(start + 1, end-1):
                    value = nums[i] + max(self.findMin(nums, start, i-1, storage), self.findMin(nums, i+1, end, storage))
                    min_value = min(min_value, value)
                storage[start][end] = min_value
        return storage[start][end]

a = Solution()
for n in range(1, 16):
    print(a.getMoneyAmount(n))