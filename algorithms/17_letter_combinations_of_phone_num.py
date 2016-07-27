# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
import random


class Solution(object):
    the_dict = {
        "0": " ",
        "1": "*",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letterCombinations(self, digits):
        base_list = [""]
        return_list = []
        for digit in digits:
            return_list = []
            for base in base_list:
                for poss in self.the_dict[digit]:
                    return_list.append(base + poss)
            base_list = return_list
        return return_list

for _ in range(100):
    print('"' + str(int(random.random() * 1000000)) + '"')