# https://leetcode.com/problems/top-k-frequent-elements/
# beats 95.48% submission
import random

class Solution(object):
    def topKFrequent(self, nums, k):
        the_dict = {}
        for n in nums:
            count = the_dict.setdefault(n, 0)
            the_dict[n] = count + 1
        the_freq_dict = {}
        for n, count in the_dict.items():
            n_list = the_freq_dict.setdefault(count, [])
            n_list.append(n)
        the_list = [d for d in the_freq_dict.keys()]
        the_list.sort(reverse=True)
        #print("the_freq_dict: ", the_freq_dict)
        #print("the_list: ", the_list)
        return_list = []
        for num in the_list:
            #print("the_freq_dict[num]: ", num, the_freq_dict[num])
            return_list.extend(the_freq_dict[num])
            #print("return_list: ", return_list)
            if len(return_list) >= k:
                return return_list
        return return_list



a = Solution()
assert(a.topKFrequent([1,1,1,2,2,3], 2) == [1,2])
assert(a.topKFrequent([9, 8, 8, 8, 8, 8, 1, 2, 3, 4, 1, 2, 3], 2) == [8, 1, 2, 3])
assert(a.topKFrequent([4,1,-1,2,-1,2,3], 2) == [-1, 2])

for i in range(0, 100):
    k = round(random.random() * 10) + 1
    pass