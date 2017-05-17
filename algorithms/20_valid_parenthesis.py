# https://leetcode.com/problems/valid-parentheses/#/description


class Solution(object):

    def isValid(self, s):
        stack = []
        open_p = ["{", "(", "["]
        close_p = ["}", ")", "]"]
        for char in s:
            if char in open_p:
                stack.append(char)
            else:
                if len(stack) == 0 or close_p.index(char) != open_p.index(stack.pop()):
                    return False
        return len(stack) == 0

a = Solution()
print(a.isValid("(())"))
print(a.isValid("([)]"))
print(a.isValid("())"))
print(a.isValid("(()"))
print(a.isValid("([{}])"))
