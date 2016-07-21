# https://leetcode.com/problems/single-number/
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution(object):
    def singleNumber(self, nums):
        a = set()
        for n in nums:
            a.add(n)
        return sum(a) * 2 - sum(nums)

a = Solution()
assert(a.singleNumber([1,2,3,2,1]) == 3)
assert(a.singleNumber([3,2,3,2,1]) == 1)
assert(a.singleNumber([1]) == 1)

