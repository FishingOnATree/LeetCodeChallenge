# https://leetcode.com/problems/anagrams/


class Solution(object):
    def groupAnagrams(self, strs):
        my_dict = {}
        for s in strs:
            index = sorted(s)
            ana_list = my_dict.setdefault("".join(index), [])
            ana_list.append(s)
        return list(my_dict.values())

a = Solution()
print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))