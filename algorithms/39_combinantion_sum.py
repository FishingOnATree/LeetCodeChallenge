# https://leetcode.com/problems/combination-sum/#/description
import random

class Solution(object):
    def combinationSum(self, candidates, target):
        result_list = []
        self.backtracking(candidates, len(candidates) - 1, target, [], result_list)
        return result_list

    def backtracking(self, candidates, n, target, base_list, result_list):
        if target == 0:
            result_list.append(base_list)
        else:
            while n >= 0 and candidates[n] > target:
                n -= 1
            if n >= 0 and candidates[n] > 0:
                new_list = list(base_list)
                new_list.append(candidates[n])
                self.backtracking(candidates, n, target - candidates[n], new_list, result_list)
                self.backtracking(candidates, n - 1, target, base_list, result_list) # not using candidate[n]


a = Solution()

print(a.combinationSum([2, 3, 6, 7], 7))
print(a.combinationSum([1], 7))
print(a.combinationSum([], 7))

for _ in range(10):
    candidates = [index for index in range(1, 11) if random.random() > 0.4]
    target = random.randint(0, 30)
    print(candidates)
    print(target)
    print(a.combinationSum(candidates, target))