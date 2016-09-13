# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.


class Solution(object):
    def longestPalindrome(self, s):
        str_start = 0
        str_end = 0
        for i in range(len(s)):
            left1, right1 = self.find_panlndrome(s, i, i)
            left2, right2 = self.find_panlndrome(s, i, i + 1)
            if right1 - left1 > right2 - left2:
                left = left1
                right = right1
            else:
                left = left2
                right = right2
            if (right - left) > (str_end - str_start):
                str_start = left
                str_end = right
        return s[str_start:str_end+1]

    def find_panlndrome(self, s, left_start, right_start):
        left = left_start
        right = right_start
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left+1, right-1

a = Solution()
print(a.longestPalindrome("abcdcbaeabcdcba"))
print(a.longestPalindrome("abbaaaaa"))
print(a.longestPalindrome("abacde"))
print(a.longestPalindrome("annonnd"))
print(a.longestPalindrome("qazhllrwnnwr"))