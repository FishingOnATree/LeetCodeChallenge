# https://leetcode.com/problems/ugly-number-ii/
#

class Solution(object):
    def nthUglyNumber(self, n):
        if n == 0:
            return 0
        else:
            base = n/3
            n2 = int(base) + 1
            n3 = int(base / 1.5) + 1
            n5 = int(base / 2.5) + 1
            #print (n, n2, n3, n5, n2 * n3 * n5)
            while n2 * n3 * n5 > n*5:
                n2p = 2 ** n2
                n3p = 3 ** n3
                n5p = 5 ** n5
                # find max
                if n2p > n3p and n2p > n5p:
                    n2 -= 1
                else:
                    if n3p > n5p:
                        n3 -= 1
                    else:
                        n5 -= 1
            #print (n, n2, n3, n5, n2 * n3 * n5)
            return_list = []
            for i in range(0, n2+1):
                for j in range(0, n3+1):
                    for k in range(0, n5+1):
                        return_list.append((2 ** i) * (3 ** j) * (5 ** k))
            return_list.sort()
            return return_list[n-1]
            # return_list = [1]
            # the_set = set()
            # the_set.add(1)
            # while len(return_list) < n:
            #     # check the multiple of the last 5 elements not in the set
            #     start_index = max(0, len(return_list) - 6)
            #     min = 0
            #     for num in return_list:
            #         for mul in (5, 3, 2):
            #             answer = num * mul
            #             if answer <= return_list[-1]:
            #                 break
            #             if answer not in the_set and (answer < min or min == 0):
            #                 min = answer
            #     return_list.append(min)
            #     the_set.add(min)
            # return return_list[-1]


a = Solution()
assert(a.nthUglyNumber(1) == 1)
assert(a.nthUglyNumber(2) == 2)
assert(a.nthUglyNumber(3) == 3)
assert(a.nthUglyNumber(4) == 4)
assert(a.nthUglyNumber(15) == 24)
assert(a.nthUglyNumber(40) == 144)
assert(a.nthUglyNumber(120) == 2700)
assert(a.nthUglyNumber(150) == 5832)
assert(a.nthUglyNumber(160) == 7200)
