# https://leetcode.com/problems/reverse-string/

class Solution(object):
    def reverseString(self, s):
        return s[::-1]

a = Solution()
assert(a.reverseString("AbCde") == "edCbA")
assert(a.reverseString("A man is there") == "ereht si nam A")
