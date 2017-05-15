# https://leetcode.com/problems/3sum-closest/#/solutions

class Solution:
    def threeSumClosest(self, num, target):
        num.sort()
        closest = num[-1] + num[-2] + num[-3]
        if closest == target:
            return closest
        else:
            for i in range(len(num) - 3):
                left, right = i+1, len(num) - 1
                while left < right:
                    total = num[i] + num[left] + num[right]
                    if total < target:
                        left += 1
                    else:
                        right -= 1
                    if abs(total - target) < abs(closest - target):
                        closest = total
                        if closest == target:
                            break
        return closest

a = Solution()
print(a.threeSumClosest([0, 2,  2, -3, 1], 0))