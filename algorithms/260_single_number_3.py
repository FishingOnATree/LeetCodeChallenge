# https://leetcode.com/problems/single-number-iii/


class Solution(object):
    def singleNumber(self, nums):
        my_set = set()
        for n in nums:
            if n in my_set:
                my_set.remove(n)
            else:
                my_set.add(n)
        return list(my_set)

a = Solution()
print(a.singleNumber([1, 2, 3, 1, 2, 3, 0, 4]))
print(a.singleNumber([1, 2, 0, 4, 2, 3, 0, 4, ]))
