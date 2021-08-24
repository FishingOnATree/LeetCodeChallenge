# https://leetcode.com/problems/132-pattern/#/description



class Solution(object):
    def find132pattern(self, nums):
        # if len(nums):
        #     min_nums = [0] * len(nums)
        #     min_nums[0] = nums[0]
        #     for i in range(1, len(nums)):
        #         min_nums[i] = min(nums[i], min_nums[i-1])
        #     right_min = nums[-1]
        #     for i in range(len(nums) - 1, 0, -1):
        #         if i < len(nums) - 1 and right_min <= nums[i]:
        #             continue
        #         else:
        #             right_min = nums[i]
        #             for j in range(i - 1, 0, -1):
        #                 if nums[j] > nums[i]
        return False


    #7.5 sec for 15000 numbers.
    def find132pattern2(self, nums):
        if len(nums):
            left_min = nums[0]
            for i in range(0, len(nums)):
                if i > 0 and nums[i] >= left_min:
                    continue
                else:
                    left_min = nums[i]
                    max_mid = nums[i]
                    for j in range(i+1, len(nums)):
                        if nums[j] >= max_mid:
                            max_mid = nums[j]
                        else:
                            if nums[i] < nums[j] < max_mid:
                                return True
        return False


a = Solution()
print(a.find132pattern([1, 1, 1, 1, 2, 1]))
print(a.find132pattern([0, 0, 0, 1, 2]))
print(a.find132pattern([3, 1, 4, 2]))
print(a.find132pattern([-1, 3, 2, 0]))
print(a.find132pattern([0, 0]))
print(a.find132pattern([]))
my_list = [i * 1 if i % 2 == 0 else i * -1 for i in range(15000)]
import timeit
timer = timeit.default_timer()
print(a.find132pattern(my_list))
print(timeit.default_timer() - timer)