# https://leetcode.com/problems/single-number-ii/
# Given an array of integers, every element appears three times except for one. Find that single one.

class Solution(object):
    def singleNumber(self, nums):
        count_dict = {}
        for n in nums:
            if n in count_dict:
                count = count_dict[n]
            else:
                count = 0
            if count >= 3:
                return n
            else:
                count_dict[n] = count + 1
        for k, v in count_dict.items():
            if v != 3:
                return k

a = Solution()
print(a.singleNumber([1, 2, 3, 1, 2, 3, 0]))
print(a.singleNumber([1, 2, 3, 1, 2, 3, 0, 0, 0, 4, 4, 4, 4]))