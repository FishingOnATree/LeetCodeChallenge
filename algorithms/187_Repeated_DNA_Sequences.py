# https://leetcode.com/problems/repeated-dna-sequences/


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        my_dict = {}
        for index in range(0, len(s) - 9):
            seq = s[index:index+10]
            my_dict.setdefault(seq, 0)
            my_dict[seq] += 1
        my_list = []
        for key, value in my_dict.items():
            if value > 1:
                my_list.append(key)
        return my_list


a = Solution()
print(a.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
