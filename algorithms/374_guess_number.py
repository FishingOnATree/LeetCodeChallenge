# https://leetcode.com/problems/guess-number-higher-or-lower/
# simple binary search

ANS = 8

class Solution(object):
    def guessNumber(self, n):
        ans = -1
        lb = 1
        guess_value = n
        while ans != 0:
            pre_guess = guess_value
            if ans < 0:
                guess_value = (guess_value+lb) // 2
                if pre_guess == guess_value:
                    guess_value -= 1
            elif ans > 0:
                lb = pre_guess
                guess_value = (lb + n) // 2
                if pre_guess == guess_value:
                    guess_value += 1
            ans = guess(guess_value)
        return guess_value

def guess(num):
    if num > ANS: return -1
    elif num < ANS: return 1
    else: return 0

a = Solution()
assert (a.guessNumber(10) == ANS)
assert (a.guessNumber(15) == ANS)
ANS = 77
assert (a.guessNumber(101) == ANS)
assert (a.guessNumber(78) == ANS)
assert (a.guessNumber(100000) == ANS)
assert (a.guessNumber(77) == ANS)
ANS = 1
assert (a.guessNumber(101) == ANS)
assert (a.guessNumber(78) == ANS)
assert (a.guessNumber(100000) == ANS)
assert (a.guessNumber(77) == ANS)
