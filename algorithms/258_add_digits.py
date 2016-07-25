# https://leetcode.com/problems/add-digits/

import random

class Solution(object):
    def addDigits(self, num):
        answer = num
        while answer >= 10:
            answer = self.add_digits(answer)
        return answer

    def add_digits(self, num):
        n = num
        answer = 0
        while n > 0:
            answer += n % 10
            n /= 10
        return answer

a = Solution()
assert(a.addDigits(208) == 1)
assert(a.addDigits(8) == 8)
assert(a.addDigits(888) == 6)
for _ in range(100):
    print(int(random.random() * 10000))
