# https://leetcode.com/problems/sum-of-two-integers/
# cannot use + and -


class Solution(object):
    def getSum(self, a, b):
        a_list = [a, b]
        return sum(a_list)


a = Solution()
assert(a.getSum(10, 11) == 10 + 11)
assert(a.getSum(121012, 12114) == 121012 + 12114)
assert(a.getSum(-1000, 14) == -1000 + 14)