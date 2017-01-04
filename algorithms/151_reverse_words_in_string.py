import re
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(re.sub(r"\s+", r" ", s.strip()).strip().split(" ")[::-1])

a = Solution()
print(a.reverseWords(" the sky is blue "))
print(a.reverseWords(" a   b "))