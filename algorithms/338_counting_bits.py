# https://leetcode.com/problems/counting-bits/


class Solution(object):
    def countBits(self, num):
        the_list = [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,1]
        power_of_2 = 32
        count = 33
        while count <= num:
            remain = count - power_of_2
            if remain == power_of_2:
                the_list.append(1)
                power_of_2 = count
            else:
                the_list.append(the_list[power_of_2] + the_list[remain])
            count += 1
        return the_list[0:(num+1)]


a = Solution()
print(a.countBits(0))
print(a.countBits(1))
print(a.countBits(2))
print(a.countBits(33))
