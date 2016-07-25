import math

class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        else:
            num = abs(n)
            ans = math.log(num, 2)
            return (2 ** int(ans)) == num


a = Solution()
for ind in range(-10,100):
    #print(ind, a.isPowerOfTwo(ind))
    print(ind)
