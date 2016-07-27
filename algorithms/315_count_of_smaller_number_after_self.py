# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# beats 91% submission on a hard problem =)
import random
import timeit

import bisect

class Solution(object):
    def countSmaller(self, nums):
        n = len(nums)
        ans = [0] * n
        sorted_list = []
        for index in range(n-1, -1, -1):
            pos = bisect.bisect_left(sorted_list, nums[index])
            ans[index] = pos
            sorted_list.insert(pos, nums[index])
        return ans

    def countSmaller_slow(self, nums):
        # O(n^2)
        n = len(nums)
        ans = []
        for index, num in enumerate(nums):
            count = 0
            for j in range(index + 1, n):
                if nums[j] < num:
                    count += 1
            ans.append(count)
        return ans


def generate_test(max_size, max_value):
    n = int(random.random() * (max_size-10)) + 10
    the_list = []
    for _ in range(n):
        the_list.append(int(random.random() * max_value))
    return the_list


a = Solution()
t1 = 0
t2 = 0
print(a.countSmaller([]))
for _ in range(1000):
    the_list = generate_test(1000, 200)
    #the_list = [19, 1, 16, 19, 4, 16, 11]
    t0 = timeit.default_timer()
    ans1 = a.countSmaller_slow(the_list)
    t1 += timeit.default_timer() - t0
    t0 = timeit.default_timer()
    ans2 = a.countSmaller(the_list)
    t2 += timeit.default_timer() - t0
    if(ans1 != ans2):
        print(the_list)
        print(sorted(the_list))
        print(a.countSmaller_slow(the_list))
        print(a.countSmaller(the_list))
print("t1 = %.4f S" % t1)
print("t2 = %.4f S" % t2)
print("FINISHED")



