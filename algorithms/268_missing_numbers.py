
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n+1) / 2
        return expected_sum - sum(nums)

a =Solution()
print(a.missingNumber([1, 2, 3]))
print(a.missingNumber([1, 2, 0]))
print(a.missingNumber([1, 0, 3]))