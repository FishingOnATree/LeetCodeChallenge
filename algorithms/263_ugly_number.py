# https://leetcode.com/problems/ugly-number/

class Solution(object):
    def isUgly(self, num):
        if num == 1:
            return True
        elif num <= 0:
            return False
        else:
            primes = [2, 3, 5]
            n = num
            for prime in primes:
                while n % prime == 0:
                    n = n / prime
            return n == 1

a = Solution()
for index in range(2, 50):
    #print(index, a.isUgly(index))
    print(index)