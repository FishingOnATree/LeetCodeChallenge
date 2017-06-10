# https://leetcode.com/problems/predict-the-winner/#/solutions

import random
import time

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if maxChoosableInteger <= 0 or (1+maxChoosableInteger)/2*maxChoosableInteger < desiredTotal:
            return False
        else:
            nums = [i+1 for i in range(maxChoosableInteger)]
        storage = {}
        return self.canWin(nums, desiredTotal, storage)

    def canWin(self, nums, desiredTotal, storage):
        #print(nums, desiredTotal)
        if nums[-1] >= desiredTotal:
            return True
        key = tuple(nums)
        if key not in storage:
            iCanWin = False
            for i in range(len(nums)):
                canTheOtherWin = self.canWin(nums[:i] + nums[i+1:], desiredTotal-nums[i], storage)
                if not canTheOtherWin:
                    iCanWin = True
                    break
            storage[key] = iCanWin
        return storage[key]

a = Solution()
start_time = time.time()
answer = a.canIWin(19, 95) #true
print("--- %s seconds ---" % (time.time() - start_time))
print(answer)
for _ in range(0):
    num = random.randint(1, 21)
    total = random.randint(1, sum([i+1 for i in range(num)]))
    print(num)
    print(total)
    start_time = time.time()
    answer = a.canIWin(num, total)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(answer)