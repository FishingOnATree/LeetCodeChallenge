# https://leetcode.com/problems/coin-change/#/description

import random

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount <= 0:
            return 0
        else:
            storage = [amount + 1] * (amount + 1)
            storage[0] = 0
            return self.countCoins(coins, amount, storage)

    def countCoins(self, coins, amount, storage):
        local_max = amount + 1
        if storage[amount] < local_max:
            return storage[amount]
        else:
            min_num = local_max
            for coin in coins:
                if coin <= amount:
                    num_coins = self.countCoins(coins, amount - coin, storage)
                    if num_coins > -1:
                        num_coins += 1
                        min_num = min(min_num, num_coins)
            storage[amount] = -1 if min_num == local_max else min_num
            return storage[amount]


a = Solution()
#print(a.coinChange([1, 2, 5], 11))
for _ in range(10):
    coins = sorted(list(set([random.randint(1, 50) for _ in range(random.randint(2, 10))])))
    print(coins)
    print(random.randint(coins[-1], coins[-1]*100))