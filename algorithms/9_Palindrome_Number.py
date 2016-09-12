# https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        x_str = str(x)
        size = len(x_str)
        front = 0
        back = size - 1
        while front < back:
            if x_str[front] == x_str[back]:
                front += 1
                back -= 1
            else:
                return False
        return True


a = Solution()
print(a.isPalindrome(123))
print(a.isPalindrome(3))
