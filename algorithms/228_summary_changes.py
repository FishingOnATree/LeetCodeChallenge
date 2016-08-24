# https://leetcode.com/problems/summary-ranges/

import random


class Solution(object):
    def summaryRanges(self, nums):
        return_list = []
        if len(nums):
            range_list = []
            range_start = nums[0]
            range_end = nums[0]
            for n in range(1, len(nums)):
                if range_end + 1 == nums[n]:
                    range_end = nums[n]
                else:
                    range_list.append(tuple((range_start, range_end)))
                    range_start = nums[n]
                    range_end = nums[n]
            range_list.append(tuple((range_start, range_end)))
            for rstart, rend in range_list:
                if rstart == rend:
                    return_list.append(str(rstart))
                else:
                    return_list.append(str(rstart) + "->" + str(rend))
        return return_list

a = Solution()
print(a.summaryRanges([]))
for _ in range(50):
    a_list = []
    for num in range(random.randint(1, 50)):
        if random.random() > 0.5:
            a_list.append(num)
    print(a_list)
    # print(a.summaryRanges(a_list))
